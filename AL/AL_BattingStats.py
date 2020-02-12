#standard libraries
import time
import os
#third party libraries
import requests
from bs4 import BeautifulSoup

pathName = os.getcwd()
print("The current working directory is %s" % pathName)
def set():
    if os.path.isdir('.\Data'):
        with open(os.getcwd() + '.\Data\AL_Batting_Stats.txt', "w") as r:
            r.write("check passed")
        print("File created in the AL\Data folder")
    else:
        try:
            os.mkdir('.\Data')
        except Exception as e:
            print("[FATAL ERROR]", e)
        else:
            with open(os.getcwd() + '.\Data\AL_Batting_Stats.txt', "w") as r:
                r.write("check passed")
            print("File created in the AL\Data folder")


#write header of data
def HeaderData():
    with open(os.getcwd() + '.\Data\AL_Batting_Stats.txt', 'w') as r:
        r.write('Batting Statistics by Player Ranking in the American Leage')
HeaderData()

#tricks website into thinking a legit browser is being used as not to throw an error
headers ={'User-Agent' : 'Mozilla/5.0'}

#go through each page until reaching 100th batter, even if non existant.
def get():
    num = 1
    while num <= 200:
        url = 'http://www.espn.com/mlb/stats/batting/_/league/al/count/{}/qualified/false'.format(num)
        res = requests.get(url, headers)
        time.sleep(1)
        if res.status_code == 200:
            soup = BeautifulSoup(res.content, 'html.parser')
            stats = soup.find('table', class_='tablehead')
            with open(os.getcwd() + '.\Data\AL_Batting_Stats.txt', 'a') as r:
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

def stats():
    set()
    get()

stats()