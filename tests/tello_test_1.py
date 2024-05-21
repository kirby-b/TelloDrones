# This script is a simple test to test turning
from djitellopy import tello
from time import sleep

drone = tello.Tello()

drone.connect()
sleep(1)
# connects
sleep(1)
drone.takeoff()
sleep(4)
# Takes off
drone.rotate_counter_clockwise(90)
sleep(6)
drone.rotate_clockwise(90)
sleep(6)
# rotates back and forth
drone.land()
# lands
drone.end()
