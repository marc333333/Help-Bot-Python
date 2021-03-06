import requests

def get_token(name):
    with open(name + ".token") as f:
        return f.readline().strip()

def get_top_definition(word):
    r = requests.get(
        url="https://mashape-community-urban-dictionary.p.rapidapi.com/define?term=" + word,
        headers = { "X-RapidAPI-Key": "f586b7f7e0mshc0b8dccb1fdd4ffp1a9b18jsn9ca3fedad99d" }		
    )
    definitions = r.json()["list"]
    return definitions[0]