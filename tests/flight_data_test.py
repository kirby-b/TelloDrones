# This script to test multi-threading and data query
from djitellopy import tello
from time import sleep
import threading
import signal

drone = tello.Tello()

def main():
    drone.connect()
    sleep(1)
    # connects
    
    t1 = threading.Thread(target=get_data, args=())
    # Makes the drone move
    t2 = threading.Thread(target=movement, args=())
 
    t1.start()
    t2.start()
 
    t1.join()
    t2.join()
    
    drone.end()


def movement():
    sleep(1)
    drone.takeoff()
    sleep(4)
    # takes off
    drone.move_up(60)
    sleep(6)
    drone.move_down(60)
    sleep(6)
    # Moves up and down
    drone.rotate_counter_clockwise(90)
    sleep(6)
    drone.rotate_clockwise(90)
    sleep(6)
    # Rotates back and forth
    drone.move_forward(100)
    sleep(6)
    drone.move_back(100)
    sleep(6)
    drone.move_left(100)
    sleep(6)
    drone.move_right(100)
    sleep(6)
    # Moves back, forward, left, right
    drone.rotate_clockwise(360)
    sleep(6)
    drone.rotate_counter_clockwise(360)
    sleep(6)
    # Rotates 360 in both directions
    drone.land()


def get_data():
    drone.query_sdk_version()
    drone.query_serial_number()
    while True:
        try:
            drone.get_barometer()
            drone.get_height()
            drone.get_battery()
            drone.get_flight_time()
            drone.get_pitch()
            drone.get_roll()
            drone.get_temperature()
            drone.get_yaw()
        except(KeyboardInterrupt):
            break
