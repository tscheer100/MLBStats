from bs4 import BeautifulSoup
import requests
import time
import os

if os.path.isdir('.\AL'):
    with open(os.getcwd() + '\\AL\\AL_Runs_Batted_in.txt', "w") as r:
        r.write("check passed")
    print("File created in the AL folder")
else:
    try:
        os.mkdir('.\AL')
    except Exception as e:
        print("[FATAL ERROR]", e)
    else:
        with open(os.getcwd() + '\\AL\\AL_Runs_Batted_in.txt', "w") as r:
            r.write("check passed")
        print("File created in the AL folder")

num = 1

headers = {'User-Agent' : 'Mozilla/5.0'}\

with open(os.getcwd() + '\\AL\\AL_Runs_Batted_in.txt', 'w') as r:
    r.write('Players Ranked by Home Runs Batted In Within the American League')

while num <= 450:
    url = 'http://www.espn.com/mlb/stats/batting/_/league/al/sort/RBIs/count/{}/qualified/false'.format(num)
    res = requests.get(url, headers)
    time.sleep(1)
    if res.status_code ==200:
        soup = BeautifulSoup(res.content, 'html.parser')
        stats = soup.find('table', class_='tablehead')
        with open(os.getcwd() + '\\AL\\AL_Runs_Batted_in.txt', 'a') as r:
            for rows in stats.find_all('tr'):
                for cell in rows.find_all('td'):
                    #Gets rid of "Sortable Batting" every once in a while.
                    if cell.text == 'Sortable Batting':
                        pass
                    else:
                        r.write(cell.text.ljust(22))
                r.write('\n')

    num+=40

