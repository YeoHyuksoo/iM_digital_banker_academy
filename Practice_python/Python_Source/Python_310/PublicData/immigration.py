from bs4 import BeautifulSoup
import urllib.request as MYURL
import lxml

serviceKey = "bEN6V0S1X1t%2F9g6gW6tw9oLyS80Et3DFdyFWk2ReJi5JaaitcpueGhEOficFv36f95iL6AHfL%2BVv7tCGaIhmbQ%3D%3D"
my_serviceKey = "Mgd249wob824izPVbUA%2BpnRSqHobrt1SbrUGC0seOwxde9Qyuq5QrYjD%2BLyhz95qNbfQ0OA%2F%2Fg3qExxFVzQvog%3D%3D"
YM = "202206"

URL = ("http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList")


URL += "?serviceKey=" + my_serviceKey
URL += "&YM=" + YM

response = MYURL.urlopen(URL)
soup = BeautifulSoup(response, "html.parser")
print(soup)

for item in soup.findAll("item"):
    print("ed: ", item.ed.string)
    print("edCd: ", item.edcd.string)
    print("natCd: ", item.natcd.string)
    print("natKorNm: ", item.natkornm.string)
    print("num: ", item.num.string)
    print("rnum: ", item.rnum.string)
    print("ym: ", item.ym.string)
    print("-----------------------------------")

