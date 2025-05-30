import json

jsonData = """
{
  "snapshot" : {
    "repos" : "test.com/repositories/snapshots",
    "userid" : "id",
    "passwd" : "1234"
  },
  "replase" : {
    "repos" : "test.com/repositories/release",
    "userid" : "id",
    "passwd" : "5678"
  },
  "component" : {
    "test" : "test.com"
  }
}
"""

data_json = json.loads(jsonData)
print(type(data_json))
print(data_json)
print(data_json["component"]["test"])

data_str = json.dumps(data_json, indent=4)
print(type(data_str))
print(data_str)
for d in data_str:
    print(d)
