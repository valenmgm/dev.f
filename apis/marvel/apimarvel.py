import requests
import keys


parameters = {
    "apikey":keys.marvelapikey,
    "ts":"1",
    "hash":keys.marvelhash,
}

resultado = ""

def getCharacter():
    fulllist = (requests.get("http://gateway.marvel.com:80/v1/public/characters", params=parameters)).json()

    for character in fulllist["data"]["results"]:
        print(character["name"])
        print(character["id"])
 #   for element in characters:
  #      print(element["name"])

getCharacter()

def characterStories():
    stories = (requests.get("http://gateway.marvel.com:80/v1/public/characters/1011031/stories", params=parameters)).json()
    for element in stories["data"]["results"]:
        print(element["title"])

characterStories()
