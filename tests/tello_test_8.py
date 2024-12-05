# This script is a stress test for the drone using most commands
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
drone.move_up(60)
sleep(6)
drone.move_down(60)
sleep(6)
# Moves up and down
drone.rotate_counter_clockwise(90)
sleep(6)
drone.rotate_clockwise(90)
sleep(6)
# Rotates back and forth
drone.move_forward(100)
sleep(6)
drone.move_back(100)
sleep(6)
drone.move_left(100)
sleep(6)
drone.move_right(100)
sleep(6)
# Moves back, forward, left, right
drone.rotate_clockwise(360)
sleep(6)
drone.rotate_counter_clockwise(360)
sleep(6)
# Rotates 360 in both directions
drone.land()
# lands
drone.end()
