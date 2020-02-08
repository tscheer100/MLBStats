import requests
from bs4 import BeautifulSoup


#get website, trick website into thinking you're using chrome.
url = 'http://www.espn.com/mlb/stats/pitching/_/sort/wins/league/al/year/2019/seasontype/2'
headers ={'User-Agent': 'Mozilla/5.0'}
res = requests.get(url, headers)

#sets soup to res and spits it out in html parsing format
soup = BeautifulSoup(res.content, 'html.parser')

#finds table from website
stats = soup.find_all('table', class_='tablehead')
stats = stats[0]

#saves the table into a text file.
with open('pitchers_stats.txt', 'w') as r:
 for row in stats.find_all('tr'):
    for cell in row.find_all('td'):
        r.write(cell.text.ljust(18))
    # divide each row by a new line
    r.write('\n')


