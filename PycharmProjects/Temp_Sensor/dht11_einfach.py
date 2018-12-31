import urllib
from bs4 import BeautifulSoup

import Python_DHT
import time
import RPi.GPIO as GPIO


starttime=time.time()


sensor = Python_DHT.DHT11

pin = 4

while True:

    feuchtigkeit, temperatur = Python_DHT.read_retry(sensor, pin)

    print("Temperatur = "+str(temperatur)+ "C Feuchtigkeit = "+str( feuchtigkeit)+"%")
    time.sleep(1)
    temp_dat = urllib.request.urlopen("https://api.thingspeak.com/update?api_key=FUCBJ4PBTRUOF25W&field1="+str(temperatur))
    hum_dat = urllib.request.urlopen("https://api.thingspeak.com/update?api_key=FUCBJ4PBTRUOF25W&field2="+str(feuchtigkeit))

    
#   grün gpio = 12
#   rot gpio = 18
#   blau gpio = 16
        
    if temperatur > float(23.0):
        print ("Der Raum ist zu warm!")
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(12,GPIO.OUT)
        GPIO.setup(16,GPIO.OUT)
        GPIO.setup(18,GPIO.OUT)
        GPIO.output(12,GPIO.LOW)
        GPIO.output(16,GPIO.LOW)
        GPIO.output(18,GPIO.HIGH)
        
    elif  float(20.0) <= temperatur <= float(23.0):
        print ("Die Temperatur is gut")
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(12,GPIO.OUT)
        GPIO.setup(16,GPIO.OUT)
        GPIO.setup(18,GPIO.OUT)
        GPIO.output(12,GPIO.HIGH)
        GPIO.output(16,GPIO.LOW)
        GPIO.output(18,GPIO.LOW)

    else:
        print ("Der Raum ist zu kalt!")
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(12,GPIO.OUT)
        GPIO.setup(16,GPIO.OUT)
        GPIO.setup(18,GPIO.OUT)
        GPIO.output(12,GPIO.LOW)
        GPIO.output(16,GPIO.HIGH)
        GPIO.output(18,GPIO.LOW)
