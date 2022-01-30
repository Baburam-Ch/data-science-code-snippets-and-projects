from bs4 import BeautifulSoup
import requests 
import csv

path = "https://coreyms.com/"

source = requests.get(path).text

soup = BeautifulSoup(source, 'html.parser')

# print(soup.prettify())

### for one article information
article = soup.find('article')
# print(article.prettify())

headline = article.h2.a.text
# print(headline)

summary = article.find('div', class_='entry-content').p.text
# print(summary)

vid_src = article.find('iframe', class_='youtube-player')['src']
vid_id = vid_src.split('/')[4].split('?')[0]
# print(vid_id)

yt_link = f'https://youtube.com/watch?v={vid_id}'
print(yt_link)

### get all articles information
articles = soup.find_all('article')

csv_file = open('cms-scraper.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'video_link'])


for article in articles:
	headline = article.h2.a.text
	print(headline)

	summary = article.find('div', class_='entry-content').p.text
	print(summary)

	try:
		vid_src = article.find('iframe', class_="youtube-player")['src']
		vid_id = vid_src.split('/')[4].split('?')[0]
		yt_link = f'https://youtube.com/watch?v={vid_id}'
	except Exception as e:
		yt_link = None
	print(yt_link)

	print()
	csv_writer.writerow([headline, summary, yt_link])
csv_file.close()
