#standard libraries
import time
import os
#third party libraries
import requests
from bs4 import BeautifulSoup

if os.path.isdir('.\Data'):
    with open(os.getcwd() + '.\Data\AL_Wins_Above_Replacement.txt', "w") as r:
        r.write("check passed")
    print("File created in the AL\Data folder")
else:
    try:
        os.mkdir('.\AL')
    except Exception as e:
        print("[FATAL ERROR]", e)
    else:
        with open(os.getcwd() + '.\Data\AL_Wins_Above_Replacement.txt', "w") as r:
            r.write("check passed")
        print("File created in the AL\Data folder")

num = 1

headers = {'User-Agent' : 'Mozilla/5.0'}

#Writes the header of the data
def HeaderData():
    with open(os.getcwd() + '.\Data\AL_Wins_Above_Replacement.txt', 'w') as r:
        r.write('Ranks players based off of placement above their replacement.')
HeaderData()

while num <= 500:
    url = 'http://www.espn.com/mlb/stats/batting/_/league/al/sort/WARBR/count/{}/qualified/false'.format(num)
    res = requests.get(url, headers)
    time.sleep(1)
    if res.status_code == 200:
        soup = BeautifulSoup(res.content, 'html.parser')
        stats = soup.find('table', class_='tablehead')
        with open(os.getcwd() + '.\Data\AL_Wins_Above_Replacement.txt', 'a') as r:
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