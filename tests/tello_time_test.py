# This is a simple test to make sure the drone can record flight time
from djitellopy import tello
from time import sleep

drone = tello.Tello()

drone.connect()
sleep(1)
# connects and sleeps to ensure it is ready

sleep(1)
drone.takeoff()
sleep(4)
drone.move_up(100)
sleep(6)
# The drone takes off and moves up to make sure the drone is considered flying
for i in range(6):
    sleep(10)
    drone.get_flight_time()
# gets the flight time every 10 seconds for 60 seconds
drone.land()
# lands
drone.end()
