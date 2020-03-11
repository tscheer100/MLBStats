#standard libraries
import time
from pathlib import Path

#third party libraries
import requests
from bs4 import BeautifulSoup

HEADERS = {'User-Agent' : 'Mozilla/5.0'}
txt = ""

def setup_path():
    global txt

    dir_path = Path(__file__).parent / "Data"
    dir_path.mkdir(exist_ok=True)

    txt = f"{dir_path}\AL_earned_run_AVG.txt"


def get_stats():
    with open(txt, "w") as f:
        f.write("Earned runs average by Player Ranking in the American League")
    print("File created in the AL\Data folder")

    max_num_players = 500
    players_per_page = 40
    for x in range(0, max_num_players, players_per_page):
        time.sleep(0.05)
        url = "http://www.espn.com/mlb/stats/pitching/_/league/al/count/{}/qualified/false/order/false".format(x)
        res = requests.get(url, HEADERS)

        if res.status_code == requests.codes.ok:
            soup = BeautifulSoup(res.content, "html.parser")
            stats = soup.find("table", class_="tablehead")

            with open(txt, "a") as f:
                for row in stats.find_all("tr"):
                    for cell in row.find_all("td"):
                        # Gets rid of "Sortable Pitching" every once in a while.
                        if cell.text == "Sortable Pitching":
                            continue
                        f.write(cell.text.ljust(25))
                    f.write("\n")
        else:
            print("no response")
            print(x)

def setup():
    setup_path()
    get_stats()


if __name__ == "__main__":
    setup()