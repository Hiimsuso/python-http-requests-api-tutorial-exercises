import requests

response = requests.get("https://assets.breatheco.de/apis/fake/sample/time.php")
json = response.json()

print(f"Current time: {json['hours']} hrs {json['minutes']} min and {json['seconds']} sec")