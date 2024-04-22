import requests
import json

client_id = 'VKF5L2ELVD4GNWHXSIKNNG34MYJ4JWVEIAVIKYLDSRYA4HMT'
client_secret = 'E14ERC54AD3M5OWKT3OHGPVVWD2WBUG5YKVUJ0AEEATLNVUO'
API_KEY = 'fsq3m4FJwH62VyfdxT7QBYCnQ8+NKID6fLnbghNzX4tB7cw='

endpoint = "https://api.foursquare.com/v3/places/search"

city = input("Введите название города (например Moscow): ")
querry = input("Введите категорию (например restaurant, cafe, library): ")

params = {
    "client_id": client_id,
    "client_secret": client_secret,
    "near": city,
    "query": querry
}

headers = {
    "Accept": "application/json",
    "Authorization": API_KEY}

response = requests.get(endpoint, params=params, headers=headers)

if response.status_code == 200:
    print("Успешный запрос API!")
    data = json.loads(response.text)
    venues = data["results"]
    for venue in venues:
        try:
            address = venue["location"]["address"]
        except KeyError:
            address = "No address"
        try:
            rating = venue["rating"]
        except KeyError:
            rating = "No rating"
        print("Название:", venue["name"])
        print("Адрес:", address)
        print("Рейтинг:", rating) 
        print("\n")

else:
    print("Запрос API завершился неудачей с кодом состояния:", response.status_code)
    print(response.text)




