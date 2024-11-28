First uninstall the old mosquitto version:

sudo apt autoremove mosquitto

then you need to add mosquitto-dev PPA to your sources list :

sudo apt-add-repository ppa:mosquitto-dev/mosquitto-ppa 
sudo apt-get update

Finally, install mosquitto:

sudo apt install mosquitto 

http://192.168.76.167:8080

Check mosquitto version :

mosquitto --version


Basic checks:

BHIoT$ sudo netstat -naltp | grep mosquitto
tcp        0      0 0.0.0.0:1883            0.0.0.0:*               LISTEN      989083/mo









