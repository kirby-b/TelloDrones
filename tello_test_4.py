from djitellopy import tello
from time import sleep

drone = tello.Tello()

drone.connect()
drone.takeoff()
sleep(3)
# connects and takes off
drone.move_up(30)
sleep(5)
drone.move_down(30)
sleep(5)
# moves up then down
drone.land()
# lands
