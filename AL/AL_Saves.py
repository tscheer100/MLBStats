#standard libraries
import time
import os
#third party libraries
import requests
from bs4 import BeautifulSoup

if os.path.isdir('.\Data'):
    with open(os.getcwd() + '.\Data\AL_Saves.txt', "w") as r:
        r.write("check passed")
    print("File created in the AL\Data folder")
else:
    try:
        os.mkdir('.\AL')
    except Exception as e:
        print("[FATAL ERROR]", e)
    else:
        with open(os.getcwd() + '.\Data\AL_Saves.txt', "w") as r:
            r.write("check passed")
        print("File created in the AL\Data folder")
num = 1

headers = {'User-Agent' : 'Mozilla/5.0'}

#Writes the header of the data
def HeaderData():
    with open (os.getcwd() + '.\Data\AL_Saves.txt', 'w') as r:
        r.write('Ranks players by number of saves in the American League')
HeaderData()

while num <= 500:
    url = 'http://www.espn.com/mlb/stats/pitching/_/league/al/sort/saves/count/{}/qualified/false'.format(num)
    res = requests.get(url, headers)
    time.sleep(1)
    if res.status_code == 200:
        soup = BeautifulSoup(res.content, 'html.parser')
        stats = soup.find()
        with open(os.getcwd() + '.\Data\AL_Saves.txt', 'a') as r:
            for rows in stats.find_all('tr'):
                for cell in rows.find_all('td'):
                    # Gets rid of "Sortable Pitching" every once in a while.
                    if cell.text == 'Sortable Pitching':
                        pass
                    else:
                        r.write(cell.text.ljust(20))
                r.write('\n')

    else:
        print("no response")
        print(num)

    num += 40