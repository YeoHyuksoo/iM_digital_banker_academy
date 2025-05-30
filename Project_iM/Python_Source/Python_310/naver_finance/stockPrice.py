from urllib import parse
from ast import literal_eval
import requests

def get_sise(code, start_time, end_time, time_from="day"):
    get_param = {
        "symbol" : code,
        "requestType" : 1, # 날짜 기준으로 조회할때 1,
        "startTime" : start_time,
        "endTime" : end_time,
        "timeframe" : time_from
    }
    get_param = parse.urlencode(get_param)
    url = "https://api.finance.naver.com/siseJson.naver?%s" % (get_param)
    response = requests.get(url)
    return literal_eval(response.text.strip())

if __name__ == "__main__":
    res = get_sise("010130", "20240102", "20241022", time_from="month")
    print(res)
    # 주가 시계열 데이터 -> 산업의 흥망에 따라서 주가가 어떻게 바뀌었는지
    # 동일 산업 분야에 다른 회사의 주가와 비교ㅏㅏ