import RPi.GPIO as GPIO

import time



#Pin 7 = GPIO4 = Right

#Pin 9 = Ground

#Pin 11 = GPIO17 = Left

#Pin 13 = GPIO27 = Forward

#Pin 15 = GPIO22 = Reverse



GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

GPIO.setup(4,GPIO.OUT)

GPIO.setup(17,GPIO.OUT)

GPIO.setup(22,GPIO.OUT)

GPIO.setup(27,GPIO.OUT)



GPIO.output(4,GPIO.LOW)

GPIO.output(17,GPIO.LOW)

GPIO.output(22,GPIO.LOW)
GPIO.output(27,GPIO.LOW)

def forward():
  print "Forward"
  GPIO.output(27, GPIO.HIGH)
  time.sleep(1)
  print "Stop"
  GPIO.output(27, GPIO.LOW)

def reverse():
  print "Reverse"
  GPIO.output(22, GPIO.HIGH)
  time.sleep(1)
  print "Stop"
  GPIO.output(22, GPIO.LOW)

def right():
  print "Right"
  GPIO.output(4, GPIO.HIGH)
  time.sleep(1)
  print "Stop"
  GPIO.output(4, GPIO.LOW)

def left():
  print "Left"
  GPIO.output(17, GPIO.HIGH)
  time.sleep(1)
  print "Stop"
  GPIO.output(17, GPIO.LOW)

forward()
right()
left()
reverse()
