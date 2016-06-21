import mraa
import time
import pyupm_i2clcd as lcd

pin2 = mraa.Gpio(2)
pin4 = mraa.Gpio(4)
pin2.dir(mraa.DIR_IN)
pin4.dir(mraa.DIR_IN)

myLcd = lcd.Jhd1313m1(0, 0x3E,0x62)

entrada1, entrada2, salida = 0,0,0 

myLcd.setCursor(0,0)
myLcd.setColor(0,0,255)
myLcd.write('AND: ')
myLcd.setCursor(1,0)

try:
        while True:
		entrada1 = pin2.read() 
        	entrada2 = pin4.read() 
        	salida = entrada1 & entrada2 
                myLcd.setCursor(1,0)
                myLcd.write("%d"%salida)
                time.sleep(1)
except:
	print "termina"

