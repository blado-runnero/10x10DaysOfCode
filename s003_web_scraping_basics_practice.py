from bs4 import BeautifulSoup
import requests

res = requests.get('http://quotes.toscrape.com/')
soup = BeautifulSoup(res.text , 'lxml')


#getting all the quotes
quotes = soup.find_all('div', {'class' : 'quote'} )


#printing one by one
for q in quotes:
	
	#extracting and printing quotes
	msg = q.find('span' , {'class' : 'text'})
	print(msg.text)

	#extracting and printing author names
	author  = q.find('small')
	print("--"+author.text)

	print()
