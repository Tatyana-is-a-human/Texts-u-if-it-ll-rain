import requests
from twilio.rest import Client
OWNENDPOINT="https://api.openweathermap.org/data/2.5/onecall"
APIKEY="2aeeb5e8b69cadcbc6cf0ffba941ee3c"
WEATHER_PARAMETERS = {
    "lat":43,
    "lon":-79,
    "exclude":"currently,minutely,daily,alerts",
    "appid":APIKEY
}


response=requests.get(url=OWNENDPOINT, params=WEATHER_PARAMETERS)
response.raise_for_status()

weather_slice=response.json()['hourly'][0:12]

will_it_rain=False

for hour in weather_slice:
    condition_code=hour["weather"][0]["id"]
    if int(condition_code)<700:
        will_it_rain=True

if will_it_rain:
    #print("bring an umbrella")

    account_sid = 'AC12de71ffbf39c8b262487fc404e72c78'
    auth_token = 'e48530b2ee3c5fdfc6f77e66b4f8ff00'
    client = Client(account_sid, auth_token)
    message = client.messages.create(body="It's gonna rain today. Bring your 'brelly!", from_="+15634122145", to='+19055368283')

    #print(message.status)

else:
    #print("It will not rain today")
