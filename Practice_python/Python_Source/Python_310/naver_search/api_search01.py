# 네이버 검색 API 예제 - 블로그 검색
import os
import sys
import urllib.request
from config import *
import datetime
import json
import csv
import sqlite3

def store_csv(filename, json_result):
    f = open(filename, "wt", encoding="utf-8", newline='')
    csv_wr = csv.writer(f)
    params = ["title", "description", "link", "bloggername", "bloggerlink", "postdate"]
    csv_wr.writerow(params)
    for res in json_result:
        tup = []
        for k, v in res.items():
            tup.append(v)
        csv_wr.writerow(tup)

    f.close()

def store_json(filename, json_result):
    with open(filename, "wt", encoding="UTF-8") as outfile:
        json.dump(json_result, outfile, indent=4, ensure_ascii = False)

def get_request_url(url):
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    try:
        response = urllib.request.urlopen(request)
        rescode = response.getcode()
        if (rescode == 200):  # http code -> ok
            response_body = response.read()
            print("[%s] Url Request Success" % datetime.datetime.now())
            return response_body.decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Url Request Fail" % datetime.datetime.now())
        return None

def getNaverSearchResult(sNode, search_text, page_start, display_n):
    base = "https://openapi.naver.com/v1/search/"
    node = "/%s.json" % sNode
    parameters = "?query=%s&start=%s&display=%s" % (urllib.parse.quote(search_text), page_start, display_n)

    url = base + node + parameters
    response_data = get_request_url(url)

    if(response_data == None):
        return None
    else:
        return json.loads(response_data)

def getPostData(post, jsonResult):
    title = post["title"]
    description = post["description"]
    bloggerlink = post["bloggerlink"]
    link = post["link"]

    postdate = post["postdate"]
    bloggername = post["bloggername"]
    jsonResult.append({"title": title, "description": description,
                       "bloggerlink": bloggerlink, "link": link,
                       "postdate": postdate, "bloggername": bloggername})
    return


def main():
    json_result = []
    sNode = 'blog'
    search_text = '한국시리즈'
    display_count = 10

    json_search = getNaverSearchResult(sNode, search_text, 1, display_count)
    while((json_search != None) and (json_search["display"] > 0)):
        for post in json_search["items"]:
            getPostData(post, json_result)

        if (int(json_search["start"]) >= 100):
            break
        # print(int(json_search["start"]))
        json_search = getNaverSearchResult(sNode, search_text, json_search["start"] + json_search["display"], display_count)
    print("-------------------------------------")
    print(json_result) #title, description, bloggerlink, link, postdate, bloggername,

    ext = ".csv"
    filename = search_text + "_naver_blog" + ext
    store_csv(filename, json_result)

    ext = ".json"
    filename = search_text + "_naver_blog" + ext
    store_json(filename, json_result)

    ext = ".db"
    tablename = search_text + "_naver_blog" + ext
    dbconn = sqlite3.connect(tablename)

    dbcursor = dbconn.cursor()
    dbcursor.execute("create table if not exists {0} \
             (title text primary key, \
                 description text, \
                 bloggerlink text, \
                link text, \
                postdate date, \
                bloggername text )".format(search_text + "_naver_blog"))

    for res in json_result:
        tup = []
        for k, v in res.items():
            tup.append(v)
        sql = "insert into {0} values (?, ?, ?, ?, ?, ?)".format(search_text + "_naver_blog")
        dbcursor.execute(sql, tup)

    dbconn.commit()

    dbcursor.close()
    dbconn.close()


if __name__ == "__main__":
    main()