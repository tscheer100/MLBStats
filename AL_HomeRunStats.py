import requests
from bs4 import BeautifulSoup
import time

#write header of data
with open('AL_Home_runs.txt', 'w') as r:
    r.write('Pitcher Statistics by Ranking.\n\n')

num = 1

#trick website into thinking a legit browser is being used as not to throw an error
headers ={'User-Agent': 'Mozilla/5.0'}

#goes to the next page over and over again until it reaches the last pitcher
while num <= 500:
    url = 'http://www.espn.com/mlb/stats/batting/_/league/al/sort/homeRuns/count/{}/qualified/false'.format(num)
    time.sleep(1)
    res = requests.get(url, headers)
    #if the page returns correctly
    if res.status_code == 200:
        soup = BeautifulSoup(res.content, 'html.parser')
        stats = soup.find('table', class_='tablehead')
        # saves the table into a text file.
        with open('AL_Home_runs.txt', 'a') as r:
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
    num += 40
