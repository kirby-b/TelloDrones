# This script is a loop test and stress test for flipping. The rotation is to test drift
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
for i in range(3):
    drone.flip("l")
    sleep(6)
    drone.rotate_clockwise(360)
    sleep(7)
    drone.flip("r")
    sleep(5)
# flips left, rotates all the way around, flips back 3 times
# It sleeps in between each so the drone doesnt error
drone.land()
# lands
drone.end()
