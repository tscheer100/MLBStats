import requests
from bs4 import BeautifulSoup
import time

with open('pitchers_stats.txt', 'w') as r:
    r.write('Pitcher Statistics by Ranking.\n\n')

num = 1

#gets the first page of picture stats from espn, trick website into thinking you're using chrome.
url = 'http://www.espn.com/mlb/stats/pitching/_/league/al/sort/wins/count/{}/qualified/false'.format(num)
headers ={'User-Agent': 'Mozilla/5.0'}

#goes to the next page over and over again until it reaches the last pitcher
while num <= 417:
    url = 'http://www.espn.com/mlb/stats/pitching/_/league/al/sort/wins/count/{}/qualified/false'.format(num)
    time.sleep(1)
    res = requests.get(url, headers)
    #if the page returns correctly
    if res.status_code == 200:
        soup = BeautifulSoup(res.content, 'html.parser')
        stats = soup.find('table', class_='tablehead')
        # saves the table into a text file.
        with open('pitchers_stats.txt', 'a') as r:
            for row in stats.find_all('tr'):
                for cell in row.find_all('td'):
                    r.write(cell.text.ljust(25))
                # divide each row by a new line
                r.write('\n')
    else:
        print("no response")
        print(num)
    num += 40









