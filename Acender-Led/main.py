import RPI.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

Led= 23

GPIO.setup(Led,GPIO.OUT)


try:
    while True:
        print("Led Aceso")
        GPIO.output(Led, True)
        time.sleep(1)
        print("Apagado")
        GPIO.output(Led, False)

except KeyboardInterrupt: print("Desligando....")