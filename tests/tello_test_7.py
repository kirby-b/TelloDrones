# This script is meant to test many of the basic movements in succession
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
drone.move_up(50)
sleep(6)
drone.move_forward(100)
sleep(6)
drone.move_down(50)
sleep(6)
drone.move_back(100)
sleep(6)
drone.rotate_clockwise(360)
sleep(6)
drone.rotate_counter_clockwise(360)
sleep(6)
# moves up, down, and rotates 360 in both direction
# It sleeps in between each so the drone doesnt error
drone.land()
# lands
drone.end()
