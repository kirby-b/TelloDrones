# This script is to test multi-threading and data query
from djitellopy import tello
from time import sleep
import threading

drone = tello.Tello()

def main():
    drone.connect()
    sleep(1)
    # Connects to drone so it can be controlled, and then
    # sleeps to make sure it is ready
    
    t1 = threading.Thread(target=get_data, args=()) 
    # Starts a data thread so we can get flight data while the drone flys
    
    t2 = threading.Thread(target=movement, args=()) 
    # Starts a movement thread so the drone can move
 
    t1.start()
    t2.start()
    # Starts the threads
 
    t1.join()
    t2.join()
    # Joins the threads so the program can end
    
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
    # Gets flight data so we can test if how it is working while the drone flys
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
