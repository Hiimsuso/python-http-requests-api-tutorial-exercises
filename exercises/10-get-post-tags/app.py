import requests

def get_post_tags(post_id):
    url = ("https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php")
    response = requests.get(url)
    json = response.json()
    for i in json['posts']:
        if i["id"] == post_id:
                return i["tags"]
        else:
            print('not found')


print(get_post_tags(146))