from djitellopy import tello
from time import sleep

drone = tello.Tello()

drone.connect()
sleep(1)
drone.takeoff()
sleep(4)
# connects and takes off
drone.move_up(50)
sleep(8)
drone.move_forward(100)
sleep(8)
drone.move_down(50)
sleep(8)
drone.move_back(100)
sleep(8)
drone.rotate_clockwise(360)
# moves up then down
drone.land()
# lands