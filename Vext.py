import requests
api_key="dIWRJ7c7.P2GZQsfcYUeGioExkCuPhw7MMdzKHS8P"
your_query="Who Is Naqib Ahmad"

headers = {
    'Content-Type': 'application/json',
    'Apikey': f'Api-Key {api_key}' 
}

data={
    "payload": your_query
}
url= 'https://payload.vextapp.com/hook/O9AZFX3D6K/catch/$(Vextwork01)'

response= requests.post(url, json=data, headers=headers)

print(response.text)