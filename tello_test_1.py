from djitellopy import tello
from time import sleep

drone = tello.Tello()

drone.connect()
drone.takeoff()
# connects and takes off
drone.rotate_counter_clockwise(90)
drone.rotate_clockwise(90)
# rotates back and forth
drone.land()
# lands