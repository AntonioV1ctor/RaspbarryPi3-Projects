import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

Led= 23

GPIO.setup(Led,GPIO.OUT)


try:
    while True:
        print("Led Aceso")
        GPIO.output(Led, True)
        time.sleep(2.5)
        print("Apagado")
        GPIO.output(Led, False)
        time.sleep(2.5)
except KeyboardInterrupt:
	print("Desligando....")
	GPIO.cleanup()
