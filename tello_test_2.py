from djitellopy import tello
from time import sleep

drone = tello.Tello()

drone.connect()
drone.takeoff()
sleep(3)
# connects and takes off
drone.flip_left()
sleep(5)
drone.flip_right()
sleep(5)
drone.flip_back()
sleep(5)
drone.flip_forward()
sleep(5)
# flips the drone left, right, backward, then forward
drone.land()
# lands
