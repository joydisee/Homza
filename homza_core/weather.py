# -*- coding: utf-8 -*-
from house import House
from internet import Internet
import logging
import requests
import datetime
import time

logger = logging.getLogger(__name__)

class WeatherCenter:

    def __init__(self):
        self.getWeather()
    
    def getWeather(self):
        house = House()
        status= {}
        # Requesting weather from OpenWeatherMap for Montreal, in .json
        try:
	        r = requests.get('http://api.openweathermap.org/data/2.5/weather?lat=%s&lon=%s&mode=json&units=metric&APPID=b55dc015063b76e0ba8531ffa35d7df6' % ( house.latitude, house.longitude ) )
            #extracting the .json data from the request
	        rj = r.json()
                # Printing the whole .json thing, with pprint() 'cause they say it's nicer
                #print rj
                #pprint(rj)
                # Temperature is called 'temp' and indented in 'main', we retrieve it
	        pressure = rj['main']['pressure']
	        temperature = rj['main']['temp']
            icon = rj['weather'][0]['icon']
	        state = rj['weather'][0]['description']
	        ID = rj['weather'][0]['id']
	        SR = rj['sys']['sunrise']
	        SS = rj['sys']['sunset']
	        wind = rj['wind']['speed']

	        sunrise = (
            	    datetime.datetime.fromtimestamp(
                	int(SR)
            	    ).strftime('%Y-%m-%d %H:%M:%S')
	        )
	        sunset = (
	            datetime.datetime.fromtimestamp(
		        int(SS)
	            ).strftime('%Y-%m-%d %H:%M:%S')
	        )
	        time_of_treatment = (
	            datetime.datetime.fromtimestamp(
		        int(time.mktime(time.localtime()))
	            ).strftime('%Y-%m-%d %H:%M:%S')
	        )
	        
	        self.time = time_of_treatment
	        self.wind = wind
	        self.sunset = sunset
	        self.sunrise = sunrise
	        self.ID = ID
	        self.state = state
	        self.pressure = pressure
	        self.temperature = temperature
	        self.icon = icon

