import RPi_I2C_driver
from time import *
import datetime
import math

from config import config
from util import *
import owapi
import lcd
from alerter import alert_queue
from dms_alerter import DMSAlerter


state = {
    'tick': 0,
    'weather_data': {},
    'marquee_weather_data': 'no weather data',
    'marquee_alert': '',
    'marquee_alive_tick_count': config['marquee_alive_ticks']
}

alerters = [DMSAlerter()]
for alerter in alerters:
    alerter.daemon = True
    alerter.start()


def poll_weather_data():
    state['weather_data'] = owapi.get_weather_data()
    state['marquee_weather_data'] = '/'.join(list(map(lambda x: x['description'], state['weather_data']['weather'])))


def poll_alert():
    if state['marquee_alive_tick_count'] >= config['marquee_alive_ticks']:
        state['marquee_alert'] = ''
    if not alert_queue.empty() and state['marquee_alert'] == '':
        message = alert_queue.get()
        speak(message)
        state['marquee_alive_tick_count'] = 0
        state['marquee_alert'] = message


def render_output():
    temp_str = '{:.0f}\xdfC'.format(ktoc(state['weather_data']['main']['temp']))
    return [
        datetime.datetime.now().strftime("%y-%m-%d %I:%M:%S%p"),
        '{} {}'.format(
            temp_str,
            render_marquee(state['tick'] / config['marquee_speed'], state['marquee_weather_data'], 20 - len(temp_str) - 1)),
        '\xd0{} \xb6{} \xc2{}%'.format(
            state['weather_data']['wind']['speed'],
            state['weather_data']['main']['pressure'],
            state['weather_data']['main']['humidity']
        ),
        render_marquee(state['tick'] / config['marquee_speed'], state['marquee_alert'], 20),
    ]


while True:
    if state['tick'] % config['weather_get_ticks'] == 0:
        poll_weather_data()
    lcd_output = render_output()
    poll_alert()

    lcd.render(lcd_output)

    state['tick'] = state['tick'] + 1
    state['marquee_alive_tick_count'] = state['marquee_alive_tick_count'] + 1
    sleep(0.1)
