# 46. JSON bilan ishlash
import json
data = {"name": "Ali"}
print(json.dumps(data))

# 47. API so‘rov (requests)
import requests
r = requests.get("https://api.github.com")
print(r.status_code)

# 48. Vaqt bilan ishlash
import datetime
print(datetime.datetime.now())

# 49. Regex
import re
s = input()
print(re.findall(r"\d+", s))

# 50. CLI argument
import sys
print(sys.argv)
