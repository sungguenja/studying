import requests
output = requests.get('https://open-api.bser.io/v1/data/ItemArmor',headers={'accept':'application/json','x-api-key':}).json()
Armor = {}
Weapon = {}
for i in output['data']:
    Armor[i['code']] = i['name']
output = requests.get('https://open-api.bser.io/v1/data/ItemWeapon',headers={'accept':'application/json','x-api-key':}).json()
for i in output['data']:
    Weapon[i['code']] = i['name']
print(Armor)
print(Weapon)