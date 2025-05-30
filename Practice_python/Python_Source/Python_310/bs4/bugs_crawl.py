from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import datetime

#bugschart_20241015.txt

def is_leapyear(year):
    if year % 4 ==0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
        else:
            return True
    return False

def get_next_day(year, month, day):
    month_31 = [1, 3, 5, 7, 8, 10, 12]
    month_30 = [4, 6, 9, 11]

    if month in month_31 and day == 31:
        day = 1
        month += 1
        if month == 13:
            year += 1
            month = 1
    elif month in month_30 and day == 30:
        day = 1
        month += 1
    elif month == 2 and ((is_leapyear(year) == True and day == 29) or (is_leapyear(year) == False and day == 28)):
        day = 1
        month += 1
    else:
        day += 1

    return year, month, day

def get_rank_data(soup):
    rank_data = []
    for data in soup.find_all("div", class_="ranking"):
        rank, change = data.text.strip().split('\n')
        rank_ele = []
        rank_ele.append(rank)
        rank_ele.append(change)
        rank_data.append(rank_ele)

    return rank_data

def get_title_data(soup):
    title_data = []
    for data in soup.find_all("p", class_="title"):
        if len(data.text.strip().split('\n')) >= 2:
            title_data.append(data.text.strip().split('\n')[len(data.text.strip().split('\n')) - 1])
        else:
            title_data.append(data.text.strip())

    return title_data

def get_artist_data(soup):
    artist_data = []
    for data in soup.find_all("p", class_="artist"):
        if len(data.find_all('a')) == 0:
            artist_data.append("서비스되지 않는 아티스트")
        for d in data.find_all('a'):
            artist_data.append(d.text.strip())
            break

    return artist_data

if __name__ == "__main__":

    now = datetime.now()
    date = input("벅스차트 일간 순위를 알아볼 날짜 범위를 입력하세요(2006.9.23 ~ %s.%s.%s) ex) 20241012 ~ 20241016\n\t\t -> " % (now.year, now.month, now.day-1))
    date_start, date_end = date.split('~')
    date_start = date_start.strip()
    date_end = date_end.strip()

    year, month, day = int(date_start[:4]), int(date_start[4:6]), int(date_start[6:])
    year_end, month_end, day_end = int(date_end[:4]), int(date_end[4:6]), int(date_end[6:])

    if year > year_end or (year == year_end and month > month_end) or (year == year_end and month == month_end and day > day_end):
        year, year_end = year_end, year
        month, month_end = month_end, month
        day, day_end = day_end, day

    if year < 2006 or (year == 2006 and month < 9) or (year == 2006 and month == 9 and day < 23):
        year = 2006
        month = 9
        day = 23

    if (year_end > now.year or (year_end == now.year and month_end > now.month)
            or (year_end == now.year and month_end == now.month and day_end > now.day)):
        year_end = now.year
        month_end = now.month
        day_end = now.day

    filename = ("bugschart_" + str(year) + str(month) + str(day) +
                '~' + str(year_end) + str(month_end) + str(day_end) + ".txt")
    f = open(filename, "wt", encoding="UTF-8")

    year_end, month_end, day_end = get_next_day(year_end, month_end, day_end)

    while year != year_end or month != month_end or day != day_end:
        date_url = str(year)
        if month < 10:
            date_url += '0'+str(month)
        else:
            date_url += str(month)
        if day < 10:
            date_url += '0'+str(day)
        else:
            date_url += str(day)
        base_url = "https://music.bugs.co.kr/chart/track/day/total?chartdate="
        html = urlopen(base_url + date_url)
        html_data = html.read().decode()
        soup = BeautifulSoup(html_data, 'html.parser')

        rank_data = get_rank_data(soup)
        title_data = get_title_data(soup)
        artist_data = get_artist_data(soup)

        data_len = len(rank_data)
        date = str(year) + '.' + str(month) + '.' + str(day)
        print("\t------------------------ 벅스 차트 %s ------------------------" % date)
        f.write("\t------------------------ 벅스 차트 %s ------------------------\n" % date)
        print(("%3s %9s %33s %24s" % ("순위", "변동 / 유지", "곡", "아티스트")))
        f.write("%3s %9s %33s %24s\n" % ("순위", "변동 / 유지", "곡", "아티스트"))

        for i in range(data_len):
            print(("%3s %9s %33s %24s" % (rank_data[i][0], rank_data[i][1], title_data[i], artist_data[i])))
            f.write("%3s %9s %33s %24s\n" % (rank_data[i][0], rank_data[i][1], title_data[i], artist_data[i]))

        print()
        f.write('\n')

        year, month, day = get_next_day(year, month, day)

    f.close()
