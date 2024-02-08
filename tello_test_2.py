from djitellopy import tello
from time import sleep

drone = tello.Tello()

drone.connect()
sleep(1)
drone.takeoff()
sleep(4)
# connects and takes off
drone.flip("l")
sleep(8)
drone.flip("r")
sleep(8)
drone.flip("f")
sleep(8)
drone.flip("b")
sleep(8)
# flips the drone left, right, backward, then forward
drone.land()
# lands
drone.turn_motor_on()
sleep(10)
drone.turn_motor_off()
# Turns the cooling motor on for 10 seconds
