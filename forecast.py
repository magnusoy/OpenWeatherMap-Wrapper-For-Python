# importing necessary libraries
import urllib.request
import json
from time import ctime

class WeatherForecast(object):
    def __init__(self):
        self.API_KEY = 'YOUR API-KEY'
        self.city = 'London'
        self.country = 'UK'
        self.request = f'http://api.openweathermap.org/data/2.5/forecast?q=%s,%s&appid=%s&units=metric'%(self.city, self.country, self.API_KEY)
    
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
