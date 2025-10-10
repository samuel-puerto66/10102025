import requests
r = requests.get("https://randomuser.me/api/")
usuario = r.json()
print(usuario)

import requests
r = requests.get("https://api.github.com")
print(respuesta.status_code)
print(respuesta.text)