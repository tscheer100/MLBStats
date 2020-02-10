import requests
from bs4 import BeautifulSoup
import time

#write header of data
with open('AL_Batting_Stats.txt', 'w') as r:
    r.write('Batting Statistics by Player Ranking in the American Leage')

num = 1

#tricks website into thinking a legit browser is being used as not to throw an error
headers ={'User-Agent' : 'Mozilla/5.0'}

#go through each page until reaching 100th batter, even if non existant.
while num <= 200:
    url = 'http://www.espn.com/mlb/stats/batting/_/league/al/count/{}/qualified/false'.format(num)
    res = requests.get(url, headers)
    time.sleep(1)
    if res.status_code == 200:
        soup = BeautifulSoup(res.content, 'html.parser')
        stats = soup.find('table', class_='tablehead')
        with open('AL_Batting_Stats.txt', 'a') as r:
            for row in stats.find_all('tr'):
                for cell in row.find_all('td'):
                    # Gets rid of "Sortable Batting" every once in a while.
                    if cell.text == 'Sortable Batting':
                        pass
                    else:
                        r.write(cell.text.ljust(25))
                r.write('\n')
    else:
        print("no response")
        print(num)

    num+=40