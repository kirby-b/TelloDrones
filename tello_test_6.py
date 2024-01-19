from djitellopy import tello
from time import sleep

drone = tello.Tello()

drone.connect()
drone.takeoff()
# connects and takes off
for i in range(3):
    drone.flip_left()
    drone.rotate_clockwise(360)
    drone.flip_right()
# flips left, rotates all the way around, flips back 3 times
drone.land()
# lands
