# Weather App in Python using openweathermap api <br>
### Output: <br>
![image](https://user-images.githubusercontent.com/70141179/104105806-cfefa480-52d6-11eb-9771-0beb0d01c408.png)

## How it works: <br>
This project takes the help of a foss API [OpenWeatherapi](https://openweathermap.org/api)<br>
OpenWeather provides historical, current and forecasted weather data via light-speed APIs<br>

From there we can subscribe the current weather data and get the api key by registering with our email-id<br>
**Steps**
<br>
1.Import the required modules.<br>
2.With the help of tkinter create a textfield to get the input from the user <br>
3.Create a function to call the api with the help of api key and the input city given by the user<br>
4.We will get the output in json format and we need to utilize it as per our requirements(Extracting the required data by using the keys)<br>
5.Create a final output string by appending all the string(data) and attach it to the label of the gui<br>
