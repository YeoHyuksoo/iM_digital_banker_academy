from bs4 import BeautifulSoup
import csv

filename = "joins.xml"
f = open(filename, 'rt', encoding = "UTF-8")
soup = BeautifulSoup(f, 'xml')

#title, link, description, author, pubDate 찾아서 화면에 출력, joins.csv파일로 저장
result_list = []

new_data = []

for data in soup.find_all(["title", "link", "description", "author", "pubDate"]):
    tag = str(data).split('>')[0][1:]
    if tag == "title":
        # print(new_data)
        if new_data:
            result_list.append(new_data)
        new_data = []

    new_data.append(data.text)


print(result_list)

with open("joins.csv", "wt", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(("title", "link", "description", "author", "pubDate"))
    writer.writerows(result_list)

