import RPi_I2C_driver

lcd = RPi_I2C_driver.lcd()

lcd_buffer = ['', '', '', '']


def render(lcd_output):
    global lcd_buffer
    for i in range(0, 4):
        if lcd_buffer[i] != lcd_output[i]:
            lcd.lcd_display_string(lcd_output[i].ljust(20), i + 1)
    lcd_buffer = lcd_output
