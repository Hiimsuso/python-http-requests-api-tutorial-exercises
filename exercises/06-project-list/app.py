import requests
response = requests.get("https://assets.breatheco.de/apis/fake/sample/project_list.php")
json = response.json()
print(json[1]['name'])