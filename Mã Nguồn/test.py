import requests


response = requests.delete("https://reqres.in/api/users/3")

print(response.json())

