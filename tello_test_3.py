from djitellopy import tello
from time import sleep

drone = tello.Tello()

drone.connect()
sleep(1)
drone.takeoff()
sleep(5)
# connects and takes off
drone.move_forward(100)
sleep(5)
# moves forward
drone.land()
# lands
