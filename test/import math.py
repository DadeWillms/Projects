import requests
import py.py as py 
from twilio.rest import Client

client = Client(py.account_sid, py.auth_token)

api_key = '40494043fc48e571e8616c1e387d017a'
user_input = input('Enter a city: ')

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

if weather_data.json()['cod'] == '404':
    print("No City Found")
else:
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])
    message = client.messages.create(
    body=f'The weather today in {user_input} is {weather}, and the temperature  is {temp}ºF',
    from_= py.twilio_nuimer,
    to=py.targert_number,
)
