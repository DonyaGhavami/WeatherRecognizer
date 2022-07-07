'''
Weather Recognizer GUI 
by Donya Ghavami
'''

import requests
import pytz
from timezonefinder import *
from pathlib import Path
from datetime import datetime
from geopy.geocoders import Nominatim
from tkinter import Label, Tk, Canvas, Entry, Text, Button, PhotoImage , messagebox

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.title("Weather App")
window.geometry("404x496")
window.configure(bg = "#FFFFFF")



canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 496,
    width = 404,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)


def weather():

    cityname = entry_2.get()

    api_key = '814694a38615faa4cfd04f243672cce4'
    api_link = 'https://api.openweathermap.org/data/2.5/weather?q='+cityname +'&appid='+ api_key

    api = requests.get(api_link).json()
    

    if api['cod'] == '404' :
        messagebox.showerror("Error" , "Invalid cityname !")

    else:

        geo = Nominatim(user_agent="geoapiExercises")
        location = geo.geocode(cityname)
        placement = TimezoneFinder()
        result = placement.timezone_at(lng = location.longitude , lat = location.latitude)
        home = pytz.timezone(result)
        local_time = datetime.now(home)

        data_time = local_time.strftime("%d %b %Y | %I:%M:%S %p")
        name.config(text = "Weather state for : ")
        clock.config(text = f"{cityname.capitalize()}  ||  {data_time}")

        tempreature_of_the_city = ((api['main']['temp'])-273.15)
        description_of_the_weather = api['weather'][0]['description']
        humidity_of_the_city = api['main']['humidity']
        speed_of_the_wind = api['wind']['speed']

        temp.config(text= f"{round(tempreature_of_the_city)} °C")
        desc.config(text = description_of_the_weather)
        humid.config(text= f"{humidity_of_the_city} %")
        speed.config(text = f"{speed_of_the_wind}  kmph")


temp = Label(window , width = 15 , height = 1 , text = "" , foreground = "#20265B" , background = "#EBF4FF" , font = ("Franklin Gothic Medium Cond" , 18))
temp.place(x = 170 , y = 270)

desc = Label(window , width = 15 , height = 1 ,  text = "" , foreground = "#20265B" , background = "#EBF4FF" , font = ("Franklin Gothic Medium Cond" , 18))
desc.place(x = 170 , y = 315 )

humid = Label(window , width = 15 , height = 1 , text = "" , foreground = "#20265B" , background = "#EBF4FF" , font = ("Franklin Gothic Medium Cond" , 18))
humid.place(x = 170 , y = 355)

speed = Label(window , width = 15 , height = 1 , text = "" , foreground = "#20265B" , background = "#EBF4FF" , font = ("Franklin Gothic Medium Cond" , 18))
speed.place(x = 170 , y = 395)

name = Label(window , background= "white" , foreground="#414545" , font =( "Franklin Gothic Medium Cond" , 14))
name.place(x= 10 , y = 170)

clock = Label(window , background= "white" , foreground="black" , font =( "Franklin Gothic Medium Cond" , 13))
clock.place(x = 143 , y = 172)


canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    31.0,
    214.0,
    371.0,
    459.0,
    fill="#EAF4FF",
    outline="")

canvas.create_text(
    53.0,
    320.0,
    anchor="nw",
    text="Description  : ",
    fill="#363D7B",
    font=("Inter", 19 * -1)
)

canvas.create_text(
    53.0,
    360.0,
    anchor="nw",
    text="Humidity : ",
    fill="#363D7B",
    font=("Inter", 19 * -1)
)

canvas.create_text(
    53.0,
    400.0,
    anchor="nw",
    text="Wind Speed :",
    fill="#363D7B",
    font=("Inter", 19 * -1)
)

canvas.create_text(
    53.0,
    275.0,
    anchor="nw",
    text="Temperature : ",
    fill="#363D7B",
    font=("Inter", 19 * -1)
)

canvas.create_text(
    108.0,
    221.0,
    anchor="nw",
    text="Weather Information ",
    fill="#000000",
    font=("Inter", 19 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    197.0,
    248.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#6F9AF0",
    highlightthickness=0
)
entry_1.place(
    x=53.0,
    y=247.0,
    width=288.0,
    height=0.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    338.0,
    128.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    244.0,
    133.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    151.0,
    134.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    63.0,
    130.0,
    image=image_image_4
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=weather,
    relief="flat"
)
button_1.place(
    x=318.0,
    y=26.0,
    width=71.0,
    height=68.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    165.0,
    57.5,
    image=entry_image_2
)
entry_2 = Entry(
    font =( "Franklin Gothic Medium Cond" , 18),  
    bd=0,
    bg="#FDFFB3",
    fg= "#cf7938" ,
    highlightthickness=0
)
entry_2.place(
    x=41.0,
    y=31.0,
    width=248.0,
    height=51.0
)
entry_2.focus()

canvas.create_text(
    40.0,
    15.0,
    anchor="nw",
    text="Enter your city name :",
    fill="#F9B788",
    font=("Inter", 13 * -1)
)


window.resizable(False, False)
window.mainloop()
