
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)

for i in range(0, 20):
    print("it is :"+str(GPIO.input(4)))
    # if GPIO.input(4) == 0:
    #     print("it is Light!")
    # else:
    #     print("it is low!")

    time.sleep(1)

    # print(GPIO.input(18))
 