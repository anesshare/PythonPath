import requests
resp = requests.get('https://pokeapi.co/api/v2/pokemon/ditto')
show = resp.json()
for line in show['game_indices']:
    print(line["version"]["name"])