import requests

def get_attachment_by_id(attachment_id):
    url = ("https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php")
    response = requests.get(url)
    json = response.json()
    for post in json['posts']:  
        if 'attachments' in post: 
            for attachment in post['attachments']:
                if attachment["id"] == attachment_id:
                    return attachment  
    print("Not found")
    return None

print(get_attachment_by_id(137))