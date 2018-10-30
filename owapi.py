import json
import urllib

from config import config
from secret import owapikey
from owdummy import owdummy


def get_weather_data():
    try:
        r = urllib.urlopen(
            'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(config['location'], owapikey))
        j = json.load(r)
        return j
    except IOError:
        return owdummy
