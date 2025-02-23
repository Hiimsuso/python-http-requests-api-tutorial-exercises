import requests

response = requests.get("https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php")
json = response.json()
print(json['posts'][0]['author']['name'])