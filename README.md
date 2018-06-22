# OpenWeatherMap Wrapper For Python
Fetches data from the Open Weather Map API and uses Python for wrapping.


You will need a valid OpenWeatherMap API key to allow responses, this script will not work without one.

You can signup for a free API key on the [Open Weather Map website](https://openweathermap.org/)


### Installing

```bash
pip install -r /path/to/requirements.txt

or

pip install requests==3.4
```


Clone or download project as zip in any directory.
Create a new python script within the directory, or copy
weather.py to your own project and import it in your
script.

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
>>> update_weather()
{'Temperature': (20, 19, 22), 'Wind': 3.1, 'Pressure': 1029, 'Humidity': 30, 'Description': 'clear sky', 'Sunrise': '05:43:30', 'Sunset': '22:21:48', 'City': 'London', 'Country': 'UK'}
		
```

## Contributing

If you want to contribute or find anything wrong, please create a Pull request, or issue adressing the change, or issue.


## Author

* **Magnus Øye** - [magnusoy](https://github.com/magnusoy)


## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/magnusoy/Arduino-with-Python/blob/master/LICENSE) file for details
