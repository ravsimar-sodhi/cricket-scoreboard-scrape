import requests
import re
from bs4 import BeautifulSoup
import csv

response = requests.get('http://www.espncricinfo.com/series/18902/scorecard/1157752/')

soup = BeautifulSoup(response.text, 'html.parser')

with open('scores.csv', mode='w') as scores:
    scores = csv.writer(scores, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for sm in soup.find_all('article', class_ ='sub-module scorecard'):
        scorebats = sm.find('div', class_ = 'scorecard-section batsmen')
        scorebowl = sm.find('div', class_ =  'scorecard-section bowling')
        
        for row in scorebats.find_all('div', class_='flex-row')[:1]:
            tRow = []
            cell = row.find('div', class_='cell')
            print(cell.string, end = '\t')
            tRow.append(cell.string)
            for sibling in cell.next_siblings:
                if sibling.string == None:
                    continue
                else:
                    print(sibling.string, end = '\t')
                    tRow.append(sibling.string)
            print()
            scores.writerow(tRow)
        for row in scorebats.find_all('div', class_='wrap batsmen'):
            tRow = []
            cell = row.find('div', class_='cell')
            print(cell.string,end='\t')
            tRow.append(cell.string)
            for sibling in cell.next_siblings:
                if sibling.string == None:
                    continue
                else:
                    print(sibling.string, end = '\t')
                    tRow.append(sibling.string)
            print()
            scores.writerow(tRow)
        print()
        scores.writerow([])
        for table in scorebowl.find_all('table'):
            for row in table.find_all('tr'):
                tRow = []
                for cell in row.find_all(['th','td']):
                    if cell.string == None:
                        continue
                    print(cell.string, end = '\t')
                    tRow.append(cell.string)
                scores.writerow(tRow)
                print()
        print()
        scores.writerow([])
