import RPi.GPIO as GPIO
import time

GPIO_PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PIN, GPIO.IN)

def motion_sensor():
    
        if(GPIO.input(GPIO_PIN) == GPIO.HIGH):
            print("in sensor")
            time.sleep(1)
            return True
        else:
            print("out sensor")
            time.sleep(1)
            return False

'''
test code
if __name__ == "__main__":
    while True:
        if motion_sensor():
            break
        else:
            continue
'''     