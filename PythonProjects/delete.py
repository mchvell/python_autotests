import requests
import json

token = '39744f028a9b042edb779b9326e1bde8'
response = requests.post('https://pokemonbattle.me:5000/pokemons/kill', headers={'trainer_token' : token}, json={
    "pokemon_id": 2840
})
print(response.text)