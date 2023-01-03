import requests
import json

token = '39744f028a9b042edb779b9326e1bde8'
'''response = requests.post('https://pokemonbattle.me:5000/pokemons', headers={'trainer_token' : token}, json={
    "name": "Mr Potatoe",
    "photo": "https://static.wikia.nocookie.net/pokemon/images/2/21/001Bulbasaur.png"
})
print(response.text)'''

response_put = requests.put('https://pokemonbattle.me:5000/pokemons', headers={'trainer_token' : token}, json={
    "pokemon_id": 2843,
    "name": "Граф Картофелина",
    "photo": ""
})
print(response_put.text)

response = requests.post('https://pokemonbattle.me:5000/trainers/add_pokeball', headers={'trainer_token' : token}, json={
      "pokemon_id": 2843
})
print(response.text)