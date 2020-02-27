#standard libraries
import time
import os
from pathlib import Path
#third party libraries
import requests
from bs4 import BeautifulSoup

# debug stuff

# pathStr = "%s" %  Path.cwd()
# print("The current working directory is ")
# print(pathStr)
# print(Path.cwd().parts[-1])

#tricks website into thinking a legit browser is being used as not to throw an error
headers ={'User-Agent' : 'Mozilla/5.0'}

def isRoot(): #https://files.gamebanana.com/img/ico/sprays/5a19d20765d97.gif
    if Path.cwd().parts[-1] == "MLBStats":
        return True
    else:
        return False

def directory():
    if isRoot():
        if Path('AL/Data').exists():
            print("AL/Data folder Already exists")
        else:
            Path('AL/Data').mkdir()
            print("Created folder AL/Data")
    else:
        if Path('Data').exists():
            print("Data folder already exists, skipping creation")
        else:
            Path('Data').mkdir()
            print("Created folder Data")
directory()

def setTxt():
    if isRoot():
        txt = 'AL/Data/AL_Batting_Stats.txt'
    else:
        txt = 'Data/AL_Batting_Stats.txt'
    return txt


def getStats():
    with open(setTxt(), "w") as r:
        r.write('Batting Statistics by Player Ranking in the American Leage')
    print("File created in the AL\Data folder")

    for x in range(0, 500,40):
        url = 'http://www.espn.com/mlb/stats/batting/_/league/al/count/{}/qualified/false'.format(x)
        res = requests.get(url, headers)
        time.sleep(0.05)

        # check if website returns correctly
        if res.status_code == 200:
            soup = BeautifulSoup(res.content, 'html.parser')
            stats = soup.find('table', class_='tablehead')

            # finds all elements in table and puts it in txt file
            with open(setTxt(), 'a') as r:
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
            print(x)

        # skip 40 players to go to next page
        x+=40


getStats()


# for begin, this was my old code before you helped me.

"""
pathName = os.getcwd()
print("The current working directory is %s" % pathName)

def directories():
    if pathName == deleted: (had to delete this because of encoding error
        if os.path.isdir('.\Data'):
            with open(os.path.join(os.getcwd(), 'Data\AL_Batting_Stats.txt'), "w") as r:
                r.write("check passed")
            print("File created in the AL\Data folder")
        else:
            try:
                os.mkdir('.\Data')
            except Exception as e:
                print("[FATAL ERROR]", e)
            else:
                with open(os.path.join(os.getcwd(), '\Data\AL_Batting_Stats.txt'), "w") as r:
                    r.write("check passed")
                print("File created in the AL\Data folder")
    else:
        if os.path.isdir('.\AL\Data'):
            with open(os.path.join(os.getcwd(), 'AL\Data\AL_Batting_Stats.txt'), "w") as r:
                r.write("check passed")
            print("File created in the AL\Data folder")
        else:
            try:
                os.mkdir('.\AL\Data')
            except Exception as e:
                print("[FATAL ERROR]", e)
            else:
                with open(os.path.join(os.getcwd(), 'AL\Data\AL_Batting_Stats.txt'), "w") as r:
                    r.write("check passed")
                print("File created in the AL\Data folder")
"""






"""
#go through each page until reaching 100th batter, even if non existant.
def get():
    num = 1
    while num <= 500:
        url = 'http://www.espn.com/mlb/stats/batting/_/league/al/count/{}/qualified/false'.format(num)
        res = requests.get(url, headers)
        time.sleep(0.05)
        if res.status_code == 200:
            soup = BeautifulSoup(res.content, 'html.parser')
            stats = soup.find('table', class_='tablehead')
            with open(os.path.join(os.getcwd(), 'AL\Data\AL_Batting_Stats.txt'), 'a') as r:
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

"""