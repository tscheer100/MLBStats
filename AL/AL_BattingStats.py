# standard libraries
import time
from pathlib import Path

# third party libraries
import requests
from bs4 import BeautifulSoup

# tricks website into thinking a legit browser is being used as not to throw an error
HEADERS = {"User-Agent": "Mozilla/5.0"}
txt = ""


def is_root():  # https://files.gamebanana.com/img/ico/sprays/5a19d20765d97.gif
    return Path.cwd().parts[-1] == "MLBStats"


def directory():
    global txt

    if is_root():
        Path("AL/Data").mkdir()
        txt = "AL/Data/AL_Batting_Stats.txt"
    else:
        Path("Data").mkdir()
        txt = "Data/AL_Batting_Stats.txt"


def getStats():
    with open(txt, "w") as r:
        r.write("Batting Statistics by Player Ranking in the American League")
    print("File created in the AL\Data folder")

    for x in range(0, 500, 40):
        url = "http://www.espn.com/mlb/stats/batting/_/league/al/count/{}/qualified/false".format(
            x
        )
        res = requests.get(url, HEADERS)
        time.sleep(0.05)

        # check if website returns correctly
        if res.status_code == 200:
            soup = BeautifulSoup(res.content, "html.parser")
            stats = soup.find("table", class_="tablehead")

            # finds all elements in table and puts it in txt file
            with open(txt, "a") as r:
                for row in stats.find_all("tr"):
                    for cell in row.find_all("td"):
                        # Gets rid of "Sortable Batting" every once in a while.
                        if cell.text == "Sortable Batting":
                            pass
                        else:
                            r.write(cell.text.ljust(25))
                    r.write("\n")
        else:
            print("no response")
            print(x)

        # skip 40 players to go to next page
        x += 40


def setup():
    directory()
    getStats()


if __name__ == "__main__":
    setup()

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

#go through each page until reaching 500th batter, even if non existant.
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
