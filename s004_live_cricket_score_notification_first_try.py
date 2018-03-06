##first draft

## at this point I am able to scrape scores only

from bs4 import BeautifulSoup
import requests


url = input('Enter url from espncrickinfo :- ')

res = requests.get(url)
soup = BeautifulSoup(res.text , 'lxml')

score = soup.find('div' , {'class' : 'cscore_score'})

print(score.text)

players = soup.find_all('td' , {'class' : 'col-highlight'})

#for i in players:
#	i = soup.find('a',{'class','short-name'})
#	print (i.text)



##I will work on this later in this week, its just that i am still unknown to how to grab data

# target date :- before 10th March


# next goals:- 
#
# 1. player name and scores 
# 2. for bowlers its scores and economy
# 3. notifications on desktop
# 4. update every 5-10 seconds

# See you later, match is getting intersting