# This script is a simple flip test
from djitellopy import tello
from time import sleep

drone = tello.Tello()

drone.connect()
sleep(1)
# connects and sleeps to ensure it is ready
sleep(1)
drone.takeoff()
sleep(4)
# takes off
drone.flip("l")
sleep(7)
drone.flip("r")
sleep(7)
drone.flip("f")
sleep(7)
drone.flip("b")
sleep(7)
# flips the drone left, right, backward, then forward. 
# It sleeps in between each so the drone doesnt error
drone.land()
# lands
drone.end()
