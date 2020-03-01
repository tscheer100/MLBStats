#standard libraries
import time
import os
#third party libraries
import requests
from bs4 import BeautifulSoup

if os.path.isdir('.\Data'):
    with open(os.getcwd() + '.\Data\AL_Home_Runs.txt', "w") as r:
        r.write("check passed")
    print("File created in the AL\Data folder")
else:
    try:
        os.mkdir('.\Data')
    except Exception as e:
        print("[FATAL ERROR]", e)
    else:
        with open(os.getcwd() + '.\Data\AL_Home_Runs.txt', "w") as r:
            r.write("check passed")
        print("File created in the AL\Data folder")



#Writes the header of the data
def HeaderData():
    with open(os.getcwd() + '.\Data\AL_Home_Runs.txt', 'w') as r:
        r.write('Pitcher Statistics by Ranking.\n\n')
HeaderData()


num = 1

#trick website into thinking a legit browser is being used as not to throw an error
headers ={'User-Agent': 'Mozilla/5.0'}

#goes to the next page over and over again until it reaches the last pitcher
while num <= 500:
    url = 'http://www.espn.com/mlb/stats/batting/_/league/al/sort/homeRuns/count/{}/qualified/false'.format(num)
    time.sleep(1)
    res = requests.get(url, headers)
    #if the page returns correctly
    if res.status_code == 200:
        soup = BeautifulSoup(res.content, 'html.parser')
        stats = soup.find('table', class_='tablehead')
        # saves the table into a text file.
        with open(os.getcwd() + '.\Data\AL_Home_Runs.txt', 'a') as r:
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
