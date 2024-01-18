from djitellopy import tello
from time import sleep

drone = tello.Tello()

drone.connect()
drone.takeoff()
# connects and takes off
drone.move_up(30)
drone.move_down(30)
# moves up then down
drone.land()
# lands
