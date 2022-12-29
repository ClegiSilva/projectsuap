import json
from xml.sax.handler import DTDHandler
import requests
api_url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(api_url)
print(response.json())
 
 
 
nome = input ("Digite o seu nome:")
username = input ("digite o seu ID:")
email = input ("qual o seu email?")
response = requests.post(api_url, json = {"name": nome, "username": username, "email":email })
print(response.json())
 
id = input ("digite o seu ID:")
response = requests.get(api_url + f"/{id}")
print(response.json())
 
id = input ('digite o seu Id:')
nome = input ("Digite o seu nome:")
response = requests.put(api_url  + f"/{id}" , json = {"nome": nome})
print(response.json())
 
id = input ("digite o seu ID:")
response = requests.delete(api_url + f"/{id}")
print(response.json())
 
 
def creat_user(user_registro):
    url = base_url +"users/"
    response = requests.post(url, json=user_registro)
    print(response.status_code)
    if response.status_code == 201:
        return response.json()
    else:
        raise ValueError('problema na execução')
print(creat_user(3))


def creat_user(user_registro):
    url = base_url +"users/"
    response = requests.post(url, json=user_registro)
    print(response.status_code)
    if response.status_code == 201:
        return response.json()
    else:
        raise ValueError('problema na execução')
print(creat_user(3))
 
 
def list_user(list_user):
    #!/usr/bin/env python3
 