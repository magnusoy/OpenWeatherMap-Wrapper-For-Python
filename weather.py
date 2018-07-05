#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""



"""

# importing necessary libraries
import urllib.request
import json
from time import ctime


class Weather(object):
    """Fetches weather forecasts

    Class which returns weather forecasts for a town/post code/zip
    using the openweathermap API"""

    def __init__(self):
        """Sets some defaults in.

        Create a new user at: https://openweathermap.org/
        and replace 'your API KEY', and write
        your own city and country"""
        self.API_KEY = 'YOUR API-KEY'
        self.city = 'London'
        self.country = 'UK'
        self.request = f'http://api.openweathermap.org/data/2.5/weather?q=%s,%s&appid=%s&units=metric'%(self.city, self.country, self.API_KEY)
        
    def __repr__(self):
        """docstring"""
        return 'City: {}, Country: {}, API_KEY: {}'.format(self.city, self.country, self.API_KEY)

    def __str__(self):
        """docstring"""
        return 'Collecting weather information for {} in {}'.format(self.city, self.country)

    def request_weather(self):
        """Requests the weather API for weather forcasts"""
        return urllib.request.urlopen(self.request).read()

    def collect_data(self):
        """Converts bytes to dictionary"""
        data = json.loads(self.request_weather())
        return data

    def get_keys(self):
        """Fetches the keys from weather dictionary"""
        weather = self.collect_data()
        return weather.keys()

    def get_coordinates(self):
        """Fetches the coordinates"""
        coords = self.collect_data()
        longitude = coords['coord']['lon']
        latitude = coords['coord']['lat']
        return longitude, latitude

    def get_temperature(self):
        """Fetches the current-, low-, and max temperature"""
        temperatures = self.collect_data()
        current_temp = temperatures['main']['temp']
        max_temp = temperatures['main']['temp_max']
        min_temp = temperatures['main']['temp_min']
        return int(current_temp), min_temp, max_temp

    def get_pressure(self):
        """Fetches the pressure"""
        pressure = self.collect_data()
        return pressure['main']['pressure']

    def get_humidity(self):
        """Fetches the humidity"""
        humidity = self.collect_data()
        return humidity['main']['humidity']

    def get_wind(self):
        """Fetches the wind speed"""
        wind = self.collect_data()
        return wind['wind']['speed']

    def get_description(self):
        """Fetches the description"""
        description = self.collect_data()
        return description['weather'][0]['description']

    def get_sunrise(self):
        """Fetches the sunrise time"""
        system = self.collect_data()
        sunrise = system['sys']['sunrise']
        clock = ctime(sunrise)
        return clock.split(' ')[-2]

    def get_sunset(self):
        """Fetches the sunset time"""
        system = self.collect_data()
        sunset = system['sys']['sunset']
        clock = ctime(sunset)
        return clock.split(' ')[-2]

    def set_city(self, city):
        """Set new city"""
        self.city = city

    def set_country(self, country):
        """Set new country"""
        self.country = country

    def set_request(self, city, country="Norway"):
        """Set new request url"""
        self.request = f'http://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid=' \
            f'{self.API_KEY}&units=metric'


def update_weather():
    """Fetches all the weather data in a dictionary"""
    weather = Weather()
    weather_data = {'Current temp': weather.get_temperature()[0],
                    'Max temp': weather.get_temperature()[1],
                    'Min temp': weather.get_temperature()[2],
                    'Wind': weather.get_wind(),
                    'Pressure': weather.get_pressure(),
                    'Humidity': weather.get_humidity(),
                    'Description': weather.get_description(),
                    'Sunrise': weather.get_sunrise(),
                    'Sunset': weather.get_sunset(),
                    'City': weather.city,
                    'Country': weather.country}
    return json.dumps(weather_data, indent=4)


if __name__ == '__main__':
    print(update_weather())
