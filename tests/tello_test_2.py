# This script is a simple flip test
from djitellopy import tello
from time import sleep

drone = tello.Tello()

drone.connect()
sleep(1)
# connects
drone.query_battery()
# gets the battery percent
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
# flips the drone left, right, backward, then forward
drone.land()
# lands
drone.end()
