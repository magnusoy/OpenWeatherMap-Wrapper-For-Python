#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""



"""

# importing necessary libraries
import urllib.request
import json
from time import ctime
import configparser

class WeatherForecast(object):
    """Fetches weather forecasts

    Class which returns weather forecasts for a town/post code/zip
    using the openweathermap API"""
    def __init__(self):
        """docstring"""
        self.Config = configparser.ConfigParser()
        self.Config.read("Config.ini")

        self.API_KEY = self.Config['forecast']['api-key']
        self.city = self.Config['forecast']['city']
        self.country = self.Config['forecast']['country']
        self.units = self.Config['forecast']['units']
        self.request = f'http://api.openweathermap.org/data/2.5/forecast?q=%s,%s&appid=%s&units=%s'%(self.city, self.country, self.API_KEY, self.units)
    
    def __str__(self):
        """docstring"""
        return 'Collecting forecast information for {} in {}'.format(self.city, self.country)

    def request_forecast(self):
        """Requests the weather API for weather forcasts"""
        return urllib.request.urlopen(self.request).read()

    def collect_data(self):
        """Converts bytes to dictionary"""
        data = json.loads(self.request_forecast())
        return data
    
    def get_keys(self):
        """Fetches the keys from weather dictionary"""
        forecasts = self.collect_data()
        return forecasts.keys()
    
    def get_forecast_data(self):
        """Fetches the list key from dictionary"""
        forecasts = self.collect_data()
        return forecasts['list']
    
    def get_forecasts(self):
        """Fetches first 4 forecasts, returns a json file"""
        forecast_number = 1
        last_day = ''
        min_temps, max_temps = [], []
        json_data = {}
        forecasts = self.get_forecast_data()
        for forecast in forecasts:
            key = ctime(forecast['dt'])
            key = key.split(' ')[0]
            if key == last_day:
                max_temps.append(forecast['main']['temp_max'])
                min_temps.append(forecast['main']['temp_min'])
            elif key != last_day and len(max_temps) > 0:
                json_data[forecast_number] = {'Day':last_day, 'Temp_max':max(max_temps), 'Temp_min':min(min_temps), 'Description':forecast['weather'][0]['description']}
                min_temps.clear()
                max_temps.clear()
                forecast_number += 1
            last_day = key
        
        return json.dumps(json_data, indent=4)

if __name__ == '__main__':
    forecast = WeatherForecast()
    print(forecast.get_forecasts())
