from djitellopy import tello
from time import sleep

drone = tello.Tello()

drone.connect()
drone.takeoff()
sleep(3)
# connects and takes off
drone.move_forward(100)
sleep(5)
# moves forward
drone.land()
# lands
