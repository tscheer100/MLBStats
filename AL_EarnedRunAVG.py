from bs4 import BeautifulSoup
import requests
import time

num = 1

headers = {'User-Agent' : 'Mozilla/5.0'}

with open('AL_Earned_Run_AVG.txt', 'w') as r:
    r.write('Players Ranked by Runs Earned Average')

while num <= 500:
    url = 'http://www.espn.com/mlb/stats/pitching/_/league/al/count/{}/qualified/false/order/false'.format(num)
    res = requests.get(url, headers)
    time.sleep(1)
    if res.status_code == 200:
        soup = BeautifulSoup(res.content, 'html.parser')
        stats = soup.find('table', class_='tablehead')
        with open('AL_Earned_Run_AVG.txt', 'a') as r:
            for rows in stats.find_all('tr'):
                for cell in rows.find_all('td'):
                    # Gets rid of "Sortable Batting" every once in a while.
                    if cell.text == 'Sortable Pitching':
                        pass
                    else:
                        r.write(cell.text.ljust(20))

    num += 40