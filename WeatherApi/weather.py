import tkinter as tk
import requests

import time

def getWeather(canvas):
    city = textfield.get()
    # http://api.openweathermap.org/data/2.5/weather?q=london&appid=c0a93f725d4dde1b8fc3fb86438e368a
    api = " http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=c0a93f725d4dde1b8fc3fb86438e368a"
    json_data =requests.get(api).json()
    cond = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] -273.15)
    # As the data temparature is in Kelvin format convert it
    min_temp = int(json_data['main']['temp_min'] -273.15)
    max_temp = int(json_data['main']['temp_max'] -273.15)    
    pressure = json_data['main']['pressure']
    humidity= json_data['main']['humidity']
    wind_speed= json_data['wind']['speed']
    # Sun rise and sun set are in seconds and we need to convert them
    sunrise  = time.strftime("%I:%M:%S",time.gmtime(json_data['sys']['sunrise']-19800))
    sunset = time.strftime("%I:%M:%S",time.gmtime(json_data['sys']['sunset']-19800))
    # for degreee symbol press alt+0176
    final_info = cond+"\n"+ str(temp)+"°C"

    final_data ="\n"+"Max Temp: "+str(max_temp)+"\n"+"Min Temp: "+str(min_temp)+"\n"+"Pressure: "+str(pressure)+"\n"+"Humidity: "+str(humidity)+"\n"+"Wind Speed: "+str(wind_speed)+"\n"+"Sun Rise: "+str(sunrise)+"\n"+ "Sun Set: "+str(sunset)+"\n"
    label1.config(text=final_info)
    label2.config(text=final_data)

                
    
    

canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")

f= ("poppins",15,"bold")
t=("poppins",35,"bold")

textfield  =tk.Entry(canvas,font =t)
textfield.pack(pady=20)
textfield.focus()
textfield.bind('<Return>',getWeather)

label1  = tk.Label(canvas,font =t )
label1.pack()
label2=tk.Label(canvas,font =f)
label2.pack()

canvas.mainloop()
