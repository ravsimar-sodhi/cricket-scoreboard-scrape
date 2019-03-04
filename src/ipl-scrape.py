import requests
import re
from bs4 import BeautifulSoup
import csv

def scrape_scoreboard(url, matchname):
    raw = requests.get(url)
    soup = BeautifulSoup(raw.text, 'html.parser')
    with open(matchname + '-batting' +'.csv', mode='w') as scores:
        with open(matchname + '-bowling' + '.csv', mode='w') as sc:
            scores = csv.writer(scores, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            sc = csv.writer(sc, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for sm in soup.find_all('article', class_ ='sub-module scorecard'):
                scorebats = sm.find('div', class_ = 'scorecard-section batsmen')
                scorebowl = sm.find('div', class_ =  'scorecard-section bowling')

                for row in scorebats.find_all('div', class_='flex-row')[:1]:
                    tRow = []
                    cell = row.find('div', class_='cell')
                    tRow.append(cell.string)
                    tRow.append('')
                    for sibling in cell.next_siblings:
                        if sibling.string == None:
                            continue
                        else:
                            tRow.append(sibling.string)
                    scores.writerow(tRow)
                scores.writerow([])
                for row in scorebats.find_all('div', class_='wrap batsmen'):
                    tRow = []
                    cell = row.find('div', class_='cell')
                    print(cell.string,end='\t')
                    tRow.append(cell.string)
                    for sibling in cell.next_siblings:
                        if sibling.string == None:
                            continue
                        else:
                            tRow.append(sibling.string)
                    scores.writerow(tRow)
                for table in scorebowl.find_all('table'):
                    for row in table.find_all('tr'):
                        tRow = []
                        for cell in row.find_all(['th','td']):
                            if cell.string == None:
                                continue
                            tRow.append(cell.string)
                        # tRow = tRow[:6] + tRow[9:]
                        sc.writerow(tRow)
                sc.writerow([])
    return

def get_url(url):
    raw = requests.get(url)
    soup = BeautifulSoup(raw.text, 'html.parser')
    l = soup.find_all('a', class_="cscore_button cscore_button--grouped button--gray button-alt sm react-router-link")
    res = []
    pref = "http://www.espncricinfo.com"
    for x in l:
        temp = pref + str(x.get('href'))
        if "scorecard" in temp:
            res.append(temp)
    return res

urllist = get_url("http://www.espncricinfo.com/scores/series/8048/season/2018/ipl")
print(urllist)
i = 1
print(len(urllist))
for x in urllist:
    name = "scoreboard-match-" + str(i)
    i += 1
    scrape_scoreboard(x, name)
