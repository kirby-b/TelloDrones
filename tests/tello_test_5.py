from djitellopy import tello
from time import sleep

drone = tello.Tello()

drone.connect()
sleep(1)
drone.takeoff()
sleep(4)
# connects and takes off
for i in range(5):
  drone.flip("l")
  sleep(8)
  drone.rotate_clockwise(360)
  sleep(8)
# flips the drone left and does a 360 clockwise 5 times
for i in range(5):
  drone.flip("r")
  sleep(8)
  drone.rotate_counter_clockwise(360)
  sleep(8)
# flips the drone left and does a 360 counter-clockwise 5 times
drone.land()
# lands
drone.turn_motor_on()
sleep(30)
drone.turn_motor_off()
# Turns the cooling motor on for 30 seconds
