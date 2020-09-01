import csv
from bs4 import BeautifulSoup
import urllib.request
# from mainfuntion import bot

def main():
	with open ('one.csv', newline='') as file:
		reader = csv.reader(file)
		data = list(reader)

	req = urllib.request.Request(
	    "https://www.spacedaily.com/",
	    headers={
	        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
	    }
	)

	webmatter = urllib.request.urlopen(req).read()

	soup = BeautifulSoup(webmatter, 'html.parser')
	body = (soup.find_all("td", {"width": "400"}))
	title_matter = (body[1].find_all("span", {"class" : "BH14"}))
	loc_matter = (body[1].find_all("span", {"class" : "BDL"}))
	title = []
	loc = []
	for i in title_matter:
		d = ""
		d += i.text
		title.append(d)
	for i in loc_matter:
		d = ""
		d += i.text
		loc.append(d)
	initial_news = []
	for i in range(len(title)):
		news = []
		news.append(title[i])
		news.append(loc[i])
		initial_news.append(news)
	final_news = []
	for i in initial_news:
		if i not in data:
			final_news.append(i)

	with open('two.csv', 'w', newline='') as file:
	    writer = csv.writer(file)
	    writer.writerow(["Headline", "Location"])
	    writer.writerows(final_news)

	with open('one.csv', 'w', newline='') as file:
	    writer = csv.writer(file)
	    writer.writerow(["Headline", "Location"])
	    writer.writerows(final_news)
	# return bot(/two.csv)

if __name__ == '__main__':
	main()