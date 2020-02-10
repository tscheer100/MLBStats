from bs4 import BeautifulSoup
import requests
import time

num = 1

headers = {'User-Agent' : 'Mozilla/5.0'}

with open('AL_Wins.txt', 'w') as r:
    r.write('Ranking of Wins  in the American League')

while num <= 500:
    url = 'http://www.espn.com/mlb/stats/pitching/_/league/al/sort/wins/count/{}/qualified/false'.format(num)
    res = requests.get(url, headers)
    time.sleep(1)
    with open('AL_Wins.txt', 'a') as r:
        if res.status_code == 200:
            soup = BeautifulSoup(res.content, 'html.parser')
            stats = soup.find('table', class_='tablehead')
            for rows in stats.find_all('tr'):
                for cell in rows.find_all('td'):
                    # Gets rid of "Sortable Pitching" every once in a while.
                    if cell.text == 'Sortable Pitching':
                        pass
                    else:
                        r.write(cell.text.ljust(20))
                r.write('\n')


    num+=40
