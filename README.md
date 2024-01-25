# TelloDrones
Programming DJI Tello Drones. Make sure to install the dji tello library before using these.

To install the dji tello library just run: **pip install djitellopy** in your command line. You may need to run the command line as admin

To run you will need a computer that can connect to wifi. Ethernet only computers cannot connect to drones as far as Im aware.

You will also need packet sender to use UDP and connect to the drone in sdk mode. In packet sender you need to make the packet: name "command" and ASCII of "command"

You can also make an ap command to connect your drone to your wifi with: name "ap" and ASCII of "ap ROUTER_SSID ROUTER_PASSWORD" . This makes it easy to create a drone swarm

Make sure both packets as under IP 192.168.10.1 ,  port 8889 , and type UDP

https://djitellopy.readthedocs.io/en/latest/tello/

https://pypi.org/project/djitellopy/

# Uses for these scripts
These scripts are not very complicated and are very basic at their core, But they can still be a fun way to learn how Tello Drones work. If you are a teacher who somehow found this repo, please feel free to use it. 
