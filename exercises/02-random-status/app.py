import requests

response = requests.get("https://assets.breatheco.de/apis/fake/sample/random-status.php")

if response == '404':
    print("The URL you asked for is not found")
elif response == '503':
    print("Unavailable right now")
elif response == '200':
    print("Everything went perfect")
elif response == '404':
    print("Something is wrong with the request params")
else:
    print("Unknown status code")