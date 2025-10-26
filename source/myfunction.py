import requests
def add(n1, n2):
    return n1 + n2

def divide(n1,n2):
    return n1/n2

def fetch_user_data(n):
    
    response = requests.get(f'https://jsonplaceholder.typicode.com/users/{n}')
    
    if response.status_code ==  200:
        return response.json()

    

def fetch_albums_data(n):
    
    response = requests.get(f'https://jsonplaceholder.typicode.com/albums/{n}')
    
    if response.status_code ==  200:
        return response.json()