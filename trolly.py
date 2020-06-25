
from time import sleep
import sys
from mfrc522 import SimpleMFRC522
import I2C_LCD_driver
from time import *
from Adafruit_IO import*

reader = SimpleMFRC522()
mylcd = I2C_LCD_driver.lcd()
maik=Client('SurabhiShrivastava','aio_ZlNv59vQZ5wFcJE4WInlXI3cnGmq')
count=0
try:
    while True:
        print("Hold a tag near the reader")
        id, text = reader.read()
        print("ID: %s\nText: %s" % (id,text))
	mylcd.lcd_display_string(id, 1)
	time.sleep(1)
	mylcd.lcd_clear()
	count=count+1;
	mylcd.lcd_display_string(count,1)
	maik.send("product",id)
        sleep(5)
except KeyboardInterrupt:
    GPIO.cleanup()
    raise
