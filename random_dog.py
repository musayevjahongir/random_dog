import requests

def random__dog():
    data=requests.get('https://dog.ceo/api/breeds/image/random')
    if data.status_code == 200:
        return data.json()['message']
    return {}

def random__cat():
    data=requests.get('https://api.thecatapi.com/v1/images/search')

    if data.status_code == 200:
        return data.json()[0]['url']    
    return {}
    
# print(random__cat())