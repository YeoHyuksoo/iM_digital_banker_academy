import json

JSON_FILE = "./test.json"
JSON_DATA = {}

def read_json(filename):
    f = open(filename, 'rt', encoding="UTF-8")
    js = json.loads(f.read())
    f.close()
    return js

def proc_json():
    JSON_DATA = read_json(JSON_FILE)

    for dic_keys in JSON_DATA:
        print(dic_keys)
        for key, val in JSON_DATA[dic_keys].items():
            print(key, " : ", val)
        print()

if __name__ == "__main__":
    proc_json()