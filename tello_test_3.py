from djitellopy import tello
from time import sleep

drone = tello.Tello()

drone.connect()
drone.takeoff()
# connects and takes off
drone.forward(100)
# moves forward
drone.land()
# lands