from djitellopy import tello

drone = tello.Tello()

drone.connect()
# Connects to the drone

drone.set_wifi_credentials('TelloDrone1!', 'Password123!')
# sets the Wi-Fi ssid and password. Definitely change these to your own.
