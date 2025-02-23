import requests

url = "https://assets.breatheco.de/apis/fake/sample/save-project-json.php"

data = {
    "id": 2323,
    "title": "Very big project"
}

response = requests.post(url, json=data, headers={"Content-Type": "application/json"})

print(response.text)