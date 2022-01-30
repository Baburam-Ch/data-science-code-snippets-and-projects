from bs4 import BeautifulSoup
import requests

# read is default
with open('simple.html') as html_file: 
	soup = BeautifulSoup(html_file, 'html.parser')

# print(soup.prettify())

### accessing the tags like attributes
# match = soup.title.text
# print(match)

# match = soup.div
# print(match)

# match = soup.find('div', class_='footer')
# print(match)

# match = soup.find('div', id='some_id')


### information of one article
article = soup.find('div', class_='article')
# print(article)

headline = article.h2.a.text
# print(headline)

summary = article.p.text
# print(summary)


### to get all of the articles
articles = soup.find_all('div', class_='article')

for article in articles:
	headline = article.h2.a.text
	print(headline)

	summary = article.p.text
	print(summary)

	print()

	
