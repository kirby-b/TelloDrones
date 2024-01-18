from djitellopy import tello
from time import sleep

drone = tello.Tello()

drone.connect()
drone.takeoff()
# connects and takes off
drone.flip_left()
drone.flip_right()
drone.flip_backward()
drone.flip_forward()
# flips the drone left, right, backward, then forward
drone.land()
# lands
