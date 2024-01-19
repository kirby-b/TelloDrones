from djitellopy import tello
from time import sleep

drone = tello.Tello()

drone.connect()
drone.takeoff()
sleep(3)
# connects and takes off
for i in range(3):
    drone.flip_left()
    sleep(5)
    drone.rotate_clockwise(360)
    sleep(5)
    drone.flip_right()
    sleep(5)
# flips left, rotates all the way around, flips back 3 times
drone.land()
# lands
