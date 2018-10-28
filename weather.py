import RPi_I2C_driver
from time import *
import urllib, json
import datetime
import math
from secret import owapikey

location = 'Waterloo'

lcd = RPi_I2C_driver.lcd()

def get_weather_data():
    r = urllib.urlopen('https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(location, owapikey))
    j = json.loads(r.read())
    return j

def ktoc(n):
    return n - 273.15

tick = 0

weatherdata = {}
lcdbuffer = ['','','','']

marquee = 'no weather data '
marquee_speed = 5

while True:
    lcdoutp = []
    try:
        if tick % 600 == 0:
            weatherdata = get_weather_data()
            marquee = '/'.join(list(map(lambda x: x['description'], weatherdata['weather']))) + ' '
        
        lcdoutp = [
            datetime.datetime.now().strftime("%y-%m-%d %I:%M:%S%p"),
            '{:.0f}\xdfC {}'.format(
                ktoc(weatherdata['main']['temp']), 
                marquee if len(marquee) <= 16 else marquee[(tick / marquee_speed) % len(marquee):(tick / marquee_speed) % len(marquee) + 16]),
            '\xd0{} \xb6{} \xc2{}%'.format(
                weatherdata['wind']['speed'],
                weatherdata['main']['pressure'],
                weatherdata['main']['humidity']
                ),
            '',
        ]
    except Exception as e:
        lcdoutp = [
                'Fatal Error'
                '{}'.format(e),
                '',
                ''
                ]
        print(e)

    for i in range(0, 4):
        if lcdbuffer[i] != lcdoutp[i]:
            lcd.lcd_display_string(lcdoutp[i].ljust(20), i + 1)

    lcdbuffer = lcdoutp
    tick = tick + 1
    sleep(0.1)
