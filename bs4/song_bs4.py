from bs4 import BeautifulSoup
filename = "./song.xml"
f = open(filename, 'rt', encoding = "UTF-8")

soup = BeautifulSoup(f.read(), 'html.parser')

#print(soup)

for song in soup.find_all("song"):
    print(song['album'])


print(soup.prettify())