#standard libraries
import time
import os
#third party libraries
import requests
from bs4 import BeautifulSoup

if os.path.isdir('.\Data'):
    with open(os.getcwd() + '.\Data\AL_Runs_Batted_in.txt', "w") as r:
        r.write("check passed")
    print("File created in the AL\Data folder")
else:
    try:
        os.mkdir('.\AL')
    except Exception as e:
        print("[FATAL ERROR]", e)
    else:
        with open(os.getcwd() + '.\Data\AL_Runs_Batted_in.txt', "w") as r:
            r.write("check passed")
        print("File created in the AL\Data folder")

num = 1

headers = {'User-Agent' : 'Mozilla/5.0'}\

#Writes the header of the data
def HeaderData():
    with open(os.getcwd() + '.\Data\AL_Runs_Batted_in.txt', 'w') as r:
        r.write('Players Ranked by Home Runs Batted In Within the American League')
HeaderData()


while num <= 450:
    url = 'http://www.espn.com/mlb/stats/batting/_/league/al/sort/RBIs/count/{}/qualified/false'.format(num)
    res = requests.get(url, headers)
    time.sleep(1)
    if res.status_code ==200:
        soup = BeautifulSoup(res.content, 'html.parser')
        stats = soup.find('table', class_='tablehead')
        with open(os.getcwd() + '.\Data\AL_Runs_Batted_in.txt', 'a') as r:
            for rows in stats.find_all('tr'):
                for cell in rows.find_all('td'):
                    #Gets rid of "Sortable Batting" every once in a while.
                    if cell.text == 'Sortable Batting':
                        pass
                    else:
                        r.write(cell.text.ljust(22))
                r.write('\n')
    else:
        print("no response")
        print(num)

    num+=40

