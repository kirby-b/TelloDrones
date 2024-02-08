from djitellopy import tello
from time import sleep

drone = tello.Tello()

drone.connect()
sleep(1)
drone.takeoff()
sleep(4)
# connects and takes off
drone.move_up(60)
sleep(8)
drone.move_down(60)
sleep(8)
# moves up then down
drone.land()
# lands
