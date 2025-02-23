import requests

def get_titles():
    titles = []
    url = ("https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php")
    response = requests.get(url)
    json = response.json()
    for i in json['posts']:
        titles.append(i['title'])
    
    return titles


print(get_titles())