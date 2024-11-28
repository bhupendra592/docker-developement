#Install broker 
-- mosquitto (Open Source Broker developed by Eclipse foundation)
#Update the latest package in apt repo (local)
--> sudo apt update
#Install mosquitto broker
--> sudo apt install mosquitto

https://mosquitto.org/

https://github.com/eclipse/mosquitto

#Publihser and Subscriber

sudo apt install mosquitto-clients

--> mosquitto_pub  [-- used to perform publish operations]

--> mosquitto_sub [-- used to perform subscriber operations]

------------------------------------------------------------------
#check broker status

sudo service mosquitto status

https://mosquitto.org/download/

allow pub and sub from diffrent systems

add these lines

cd /etc/mosquitto/conf.d

sudo nano ipallow.conf

bind_address 0.0.0.0
allow_anonymous true

sudo service mosquitto restart

----------------------------------------------
#Sample output 
sudo netstat -naltp | grep mosquitto 

tcp        0      0 0.0.0.0:1883            0.0.0.0:*               LISTEN      1736/mosquitto
---------------------------------------------------------
#Terminal-1
Publisher Client: (Like an IoT Device)

mosquitto_pub -t cdac/acts/desd/temp  -h 127.0.0.1 -p 1883 -m "temperature is 20C"

-h (host which is broker address)

-t (topic name)

-p -- port number

-m - (Send a single message and disconnect)

#Terminal 2

Subscriber : Mostly IoT platform or IoT Gateway 

mosquitto_sub -t cdac/acts/desd/temp -h 127.0.0.1 -p 1883 

-----------------------------------------------------------

Publish Message Line by line (stdin)

mosquitto_pub -t cdac/acts/desd/temp  -h 127.0.0.1 -p 1883 -l

ToDo:
--------
1 . Host Machine-1 (Pub + Broker)
2. HostMachine-2 (sub)
-----------------------------------
1. HostMachine-1 (Pub)
2. Hostmachine-2 (sub)
3. Hostmachine-3 (broker)
---------------------------------
1 . Host Machine -1 (Pub)
2. Host Machine (Broker + sub)


-h and -p field is optional in case the same host broker is used

Example:

mosquitto_sub -t cdac/acts 


#Public broker

https://test.mosquitto.org/









