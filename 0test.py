import requests
import json

resp = requests.get('http://127.0.0.1:8000/aprests/')
if resp.status_code != 200:
    raise ValueError('GET /aprests/ {}'.format(resp.status_code))

j = dict(resp.json())


for result in j['results']:
    print("\n", result["url"], result["title"])

print(f"There are {len(result) + 1} results.")


print(j.items())


