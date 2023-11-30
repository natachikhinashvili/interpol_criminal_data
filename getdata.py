import requests
import json

response=requests.get("https://ws-public.interpol.int/notices/v1/red")

jsonresponse = response.json()

with open('data.json', 'w') as f:
    json.dump(jsonresponse, f)