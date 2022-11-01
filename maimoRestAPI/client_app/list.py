import requests
from getpass import getpass

auth_endpoint = "http://localhost:8000/auth/"
username = input("Enter Your Username:\t")
password = getpass("Enter your password:\t")


auth_response = requests.post(auth_endpoint, json={'username': username, 'password':password })
#print(auth_response.json())

if auth_response.status_code==200:
    token = auth_response.json()['token']
    headers = {
        #'Authorization': f"Token {token}"
        'Authorization': f"Bearer {token}"
    }
    endpoint = "http://localhost:8000/api/list/"

    response = requests.get(endpoint, headers=headers) 
    print(response.json())