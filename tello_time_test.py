from djitellopy import tello
from time import sleep

drone = tello.Tello()

drone.connect()
sleep(1)
drone.takeoff()
sleep(4)
# connects and takes off
drone.move_up(100)
for i in range(6):
    sleep(10)
    drone.get_flight_time()
# Turns on the camera and shows front and down view
drone.land()
# lands