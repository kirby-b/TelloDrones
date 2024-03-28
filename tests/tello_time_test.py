from djitellopy import tello
from time import sleep

drone = tello.Tello()

drone.connect()
sleep(1)
# connects
drone.query_battery()
# gets the battery percent
sleep(1)
drone.takeoff()
sleep(4)
# takes off
drone.move_up(100)
sleep(6)
for i in range(6):
    sleep(7)
    drone.get_flight_time()
# gets the flight time every 10 seconds for 60 seconds
drone.land()
# lands
drone.end()
