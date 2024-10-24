import json
import urllib.request

# stock_code = "005930"
# url = "https://m.stock.naver.com/api/stock/%s/integration" % (stock_code)
# raw_data = urllib.request.urlopen(url).read()
# json_data = json.loads(raw_data)
#
# print(json_data)

stock_code = "005930"
url = "https://m.stock.naver.com/api/stock/%s/integration" % (stock_code)
raw_data = urllib.request.urlopen(url).read()
json_data = json.loads(raw_data)

stock_name = json_data["stockName"]
print("종목명 : %s" % stock_name)

print(json_data)

date = json_data["dealTrendInfos"][0]["bizdate"]
price = json_data["dealTrendInfos"][0]["closePrice"]
print("%s의 마감 가격 : %s" % (date, price))

for attr in json_data["totalInfos"]:
    if "marketValue" == attr["code"]:
        marketSum_val = attr["value"]
        print("시총 : %s" % marketSum_val)

    elif "per" == attr["code"]:
        per_val_str = attr["value"]
        print("PER : %s" % per_val_str)

    elif "pbr" == attr["code"]:
        pbr_val_str = attr["value"]
        print("PBR : %s" % pbr_val_str)
