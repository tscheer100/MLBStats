#standard libraries
import time
import os
#third party libraries
import requests
from bs4 import BeautifulSoup

pathName = os.getcwd()
print("The current working directory is %s" % pathName)

def directories():
    if pathName == r"C:\Users\Turtle\PycharmProjects\MLBStats\AL":
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

directories()


#write header of data
def HeaderData():
    with open(os.path.join(os.getcwd(), 'AL\Data\AL_Batting_Stats.txt'), 'w') as r:
        r.write('Batting Statistics by Player Ranking in the American Leage')
HeaderData()

#tricks website into thinking a legit browser is being used as not to throw an error
headers ={'User-Agent' : 'Mozilla/5.0'}

#go through each page until reaching 100th batter, even if non existant.
def get():
    num = 1
    while num <= 4000:
        url = 'http://www.espn.com/mlb/stats/batting/_/league/al/count/{}/qualified/false'.format(num)
        res = requests.get(url, headers)
        time.sleep(1)
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




#uncomment the command below if running file directly
get()
