import requests 

response = requests.get('https://servicodados.ibge.gov.br/api/v1/localidades/distritos')

distritos = response.json()
for distrito in distritos: 
    print(distritos['nome']) 
