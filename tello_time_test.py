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
# gets the flight time every 10 seconds for 60 seconds
drone.land()
# lands
