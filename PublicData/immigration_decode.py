from bs4 import BeautifulSoup
import urllib.request as MYURL
import requests

serviceKey = "bEN6V0S1X1t/9g6gW6tw9oLyS80Et3DFdyFWk2ReJi5JaaitcpueGhEOficFv36f95iL6AHfL+Vv7tCGaIhmbQ=="

params = {"serviceKey": serviceKey, "YM": "202203", "NAT_CD": "112", "ED_CD": "E"}

URL = ("http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList")
response = requests.get(URL, params = params)
response = response.content.decode(encoding="UTF-8", errors="strict")
print(response)

soup = BeautifulSoup(response, "html.parser")

for item in soup.findAll("item"):
    print("ed: ", item.ed.string)
    print("edCd: ", item.edcd.string)
    print("natCd: ", item.natcd.string)
    print("natKorNm: ", item.natkornm.string)
    print("num: ", item.num.string)
    print("rnum: ", item.rnum.string)
    print("ym: ", item.ym.string)
    print("-----------------------------------")

