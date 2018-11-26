import requests

class Weather:
    def __init__(self, weatherParams):
        self.weatherRequestParams = weatherParams
        self.askForCityName()

    def askForCityName(self):
        city = input("Hi.  What city's weather forecast would you like to hear about?")
        print(city)
        weatherData = requests.get('http://api.openweathermap.org/data/2.5/weather?q={}&units={}'.format(city, "imperial"), params = self.weatherRequestParams).json()
        weatherMain = list(weatherData['weather'])[0]['main']
        weatherDescription = list(weatherData['weather'])[0]['description']
        mainTemp = weatherData['main']['temp']
        mainTempMin = weatherData['main']['temp_min']
        mainTempMax = weatherData['main']['temp_max']
        print("Looks like the weather is as follows in {}:\nMain: {}\nDescription: {}\nTemp: {} Farenheit\nTempMin: {} Farenheit\nTempMax: {} Farenheit\n".format(city, weatherMain, weatherDescription, str(mainTemp), str(mainTempMin), (mainTempMax)))

if __name__== "__main__":
    print("Main Program")
    weatherRequestParams = {'APPID': '8a25393ce069125236a34d22ef0a2615'}
    weatherForecast = Weather(weatherRequestParams)
    weatherForecast.askForCityName()
