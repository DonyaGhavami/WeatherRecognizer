'''
Weather Recognizer
by Donya Ghavami

'''

import requests
from os import system 
from datetime import datetime

system("cls")

api_key = '814694a38615faa4cfd04f243672cce4'

cityname = input("Enter the name of the city : ")

api_link = 'https://api.openweathermap.org/data/2.5/weather?q='+cityname +'&appid='+ api_key

api = requests.get(api_link).json()


if api['cod'] == '404' :
    print(f"Invalid city name : {cityname} , please check. ")

else:
    
    tempreature_of_the_city = ((api['main']['temp'])-273.15)
    description_of_the_weather = api['weather'][0]['description']
    humidity_of_the_city = api['main']['humidity']
    speed_of_the_wind = api['wind']['speed']
    data_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")


    print('*'*30)
    print(f"weather states for : {cityname.capitalize()} || {data_time}.")
    print('*'*30)


    print(f"current tempreature is : {round(tempreature_of_the_city)} °C . ")
    print("description of the current weather is : " , description_of_the_weather)
    print("current humidity is : " , humidity_of_the_city , '%')
    print("the wind speed of the current weather is : " , speed_of_the_wind , 'kmph')
































#https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}