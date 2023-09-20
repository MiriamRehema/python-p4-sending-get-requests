import requests
import json

url = "http://rivals.yahoo.com/ncaa/basketball/teams/iai/endpoints/locations.json"

response = requests.get(url)
print(response.content)

json_content = json.loads(response.text)

print(json.dumps(json_content, indent=4))
