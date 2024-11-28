# Where does the persistent session details are stored in?

-- MQTT DB file 

# Path - Navigate to

cd /var/lib/mosquitto

--> ls 

mosquitto.db    #this is the default file which maintains the retain and persistent session data

# How to read mosquitto.db file?
----------------------------------------------------------
git clone https://github.com/eclipse/mosquitto

cd mosquitto/apps/db_dump

make

sudo ./mosquitto_db_dump /var/lib/mosquitto/mosquitto.db
----------------------------------------------------------
# Retain Message (last known good value) use -r flag

HIoT$ mosquitto_pub -t cdac/retain -h localhost -p 1883 -l -d -r
Client null sending CONNECT
Client null received CONNACK (0)
1 
Client null sending PUBLISH (d0, q0, r1, m1, 'cdac/retain', ... (1 bytes))
2
Client null sending PUBLISH (d0, q0, r1, m2, 'cdac/retain', ... (1 bytes))
3
Client null sending PUBLISH (d0, q0, r1, m3, 'cdac/retain', ... (1 bytes))
4
Client null sending PUBLISH (d0, q0, r1, m4, 'cdac/retain', ... (1 bytes))
5
Client null sending PUBLISH (d0, q0, r1, m5, 'cdac/retain', ... (1 bytes))
6
^C

# Above the client is disconneted and subscriber has not yet subscribed the topic

------------------------
# Observe the output - At Subscriber end
BHIoT$ mosquitto_sub -t cdac/retain -h localhost -p 1883
6

# How to Discard the retain message: (Publish the null message)
------------------------------
BHIoT$ mosquitto_pub -t cdac/retain -h localhost -p 1883 -r -n -d
Client null sending CONNECT
Client null received CONNACK (0)
Client null sending PUBLISH (d0, q0, r1, m1, 'cdac/retain', ... (0 bytes))
Client null sending DISCONNECT
----------------------------------------------------------------------------
BHIoT$ mosquitto_pub -t cdac/retain -h localhost -p 1883 -r -m "" -d
Client null sending CONNECT
Client null received CONNACK (0)
Client null sending PUBLISH (d0, q0, r1, m1, 'cdac/retain', ... (0 bytes))
Client null sending DISCONNECT
-------------------------------------------------------------------------------