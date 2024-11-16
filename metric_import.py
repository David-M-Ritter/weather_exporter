from time import sleep
import requests
import argparse


parser = argparse.ArgumentParser()

parser.add_argument('--dt_url',       type=str, required=True)
parser.add_argument('--dt_api_token', type=str, required=True)
x = vars(parser.parse_args())


class temp():
    def __init__(self, town:str, weather_api_url:str):
        self.town = town
        self.weather_api_url = weather_api_url

    def get_temp(self):
        y = requests.get(self.weather_api_url)
        y_response = str(y.json()).split(": ")
        temp = str(y_response[(len(y_response)-1)].removesuffix("}}"))
        y.close()
        print(temp)
        return temp

    def post_temp(self, temperature):
        requests.post(x["dt_url"] + "api/v2/metrics/ingest?Api-Token=" + x['dt_api_token'], data=("city.temperature.fahrenheit,city.name=" + self.town + " "+ temperature))
        

temp_chx:str = "https://api.open-meteo.com/v1/forecast?latitude=45.3181&longitude=-85.2584&current=temperature_2m&temperature_unit=fahrenheit&wind_speed_unit=mph&precipitation_unit=inch&forecast_days=1"
temp_lan:str = "https://api.open-meteo.com/v1/forecast?latitude=42.7325&longitude=-84.5555&current=temperature_2m&temperature_unit=fahrenheit&wind_speed_unit=mph&precipitation_unit=inch&forecast_days=1"
temp_lud:str = "https://api.open-meteo.com/v1/forecast?latitude=43.9553&longitude=-86.4526&current=temperature_2m&temperature_unit=fahrenheit&wind_speed_unit=mph&precipitation_unit=inch&forecast_days=1"
temp_syd:str = "https://api.open-meteo.com/v1/forecast?latitude=-33.8678&longitude=151.2073&current=temperature_2m&temperature_unit=fahrenheit&wind_speed_unit=mph&precipitation_unit=inch&forecast_days=1"
temp_par:str = "https://api.open-meteo.com/v1/forecast?latitude=48.8534&longitude=2.3488&current=temperature_2m&temperature_unit=fahrenheit&wind_speed_unit=mph&precipitation_unit=inch&forecast_days=1"

charlevoix:object = temp("Charlevoix", temp_chx)
Lansing:object    = temp("Lansing",    temp_lan)
Ludington:object  = temp("Ludington",  temp_lud)
Sydney:object     = temp("Sydney",     temp_syd)
Paris:object      = temp("Paris",      temp_par)

while True:
    try:
        charlevoix.post_temp(   charlevoix.get_temp())
        Lansing.post_temp(      Lansing.get_temp())
        Ludington.post_temp(    Ludington.get_temp())
        Sydney.post_temp(       Sydney.get_temp())
        Paris.post_temp(        Paris.get_temp())
    
    except Exception as e:
        print(e)

    sleep(60)