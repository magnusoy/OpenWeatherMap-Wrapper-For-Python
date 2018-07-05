# OpenWeatherMap Wrapper For Python
Fetches data from the Open Weather Map API and uses Python for wrapping.


You will need a valid OpenWeatherMap API key to allow responses, this script will not work without one.

You can signup for a free API key on the [Open Weather Map website](https://openweathermap.org/)


### Installing
Only requires requests, which you can simply download with pip. 

```bash
pip install requests==3.4
```

### Examples

```python
>>> from weather import Weather
>>> weather = Weather()
>>> weather.get_temperature()
(20, 20, 21)
>>> weather.get_description()
'clear sky'

```

```python
>>> from weather import update_weather
>>> print(update_weather())
{
    "Current temp": 21,
    "Max temp": 18,
    "Min temp": 25,
    "Wind": 2.6,
    "Pressure": 1016,
    "Humidity": 60,
    "Description": "clear sky",
    "Sunrise": "05:51:20",
    "Sunset": "22:18:43",
    "City": "London",
    "Country": "UK"
}
```

```python
>>> from forecast import WeatherForecast
>>> forecast = WeatherForecast()
>>> print(forecast.get_forecasts())
{
    "1": {
        "Day": "Fri",
        "Temp_max": 28.47,
        "Temp_min": 12.38,
        "Description": "clear sky"
    },
    "2": {
        "Day": "Sat",
        "Temp_max": 28.75,
        "Temp_min": 18.32,
        "Description": "clear sky"
    },
    "3": {
        "Day": "Sun",
        "Temp_max": 29.79,
        "Temp_min": 16.83,
        "Description": "clear sky"
    },
    "4": {
        "Day": "Mon",
        "Temp_max": 31.39,
        "Temp_min": 18.79,
        "Description": "clear sky"
    }
}
```
## Contributing

If you want to contribute or find anything wrong, please create a Pull request, or issue adressing the change, or issue.


## Author

* **Magnus Øye** - [magnusoy](https://github.com/magnusoy)


## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/magnusoy/Arduino-with-Python/blob/master/LICENSE) file for details
