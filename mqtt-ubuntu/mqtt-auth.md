# User based Authentication in MQTT
----------------------------------------

# Step 1 

Create a user with encrupted password for broker

BHIoT$ sudo touch /etc/mosquitto/userauth

sudo chmod 700 /etc/mosquitto/userauth

sudo chown mosquitto:mosquitto /etc/mosquitto/userauth


BHIoT$ sudo mosquitto_passwd -b /etc/mosquitto/userauth desd desd123

BHIoT$ sudo cat /etc/mosquitto/userauth 
desd:$7$101$rYcyNnfyvBx9ddUG$GJ0s9WJg+sTi2O4MKn7JOXyhrqwq2yA0a6NIAB1x0CLl86UGeapgxouMV7oPJwEypp7AUU32l1xbdzXlwP+OMg==
--------------------------------------------

#conf file contents - location /etc/mosquitto/conf.d

allow_anonymous false     #true -> No auth is required
listener 1883 0.0.0.0
password_file /etc/mosquitto/userauth

#Restart the Broker

sudo service mosquitto restart

#test without username and password

BHIoT$ mosquitto_pub -t cdac/acts -l
Connection error: Connection Refused: not authorised.
Error: The connection was refused.


tail -f /var/log/mosquitto.log






