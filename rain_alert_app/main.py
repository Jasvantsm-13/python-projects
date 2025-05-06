import requests
from twilio.rest import Client

OWM_Endpoint = "https://pro.openweathermap.org/data/2.5/forecast"
api_key = "b0bba4ac4f170528e62f7e45683f7f5b"

account_sid = "AC849decea2c3bf83cdd889c339xxxxxxxxx" # geting this from sign in twilio and create account

auth_token = "fc78dc195d6845ee29a3fa28d78dxxxxxxx"

weather_params = {
    "lat" : 23.237560,
    "lon" : 72.647781,
    "appid" : api_key,
    "cnt" : 4,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

# print(weather_data)

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
    if will_rain:
        client = Client(account_sid, auth_token)
        message = client.messages.create(

            body="it's going to rain today. Remember to bring an umbrella",

            from_="+12549982728",# created by twilio

            to="+917574xxxxxx", # my number 

        )
        print(message.status)


