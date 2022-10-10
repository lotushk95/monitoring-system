import cv2
import os
import requests
import RPi.GPIO as GPIO
import time

from camera import camera
from motion_sensor import motion_sensor
from face_detect import face_detect
from line import send_message
from line import send_message_and_image

SAVEDIR = ""
STATUS = 'face is detected!'

GPIO_PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PIN, GPIO.IN)

line_notify_token = ""
url = 'https://notify-api.line.me/api/notify'


if __name__ == "__main__":
    
    while(True):
        
        if motion_sensor():
            filename = camera()
            filename, is_detected = face_detect(filename)
            if is_detected:
                print(STATUS)
                send_message_and_image(STATUS, filename)
            else:
                print('face is not detected!')
                send_message('face is not detected!')