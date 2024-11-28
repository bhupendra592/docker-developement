# Topic covered
1. Keep Alive
2. Last Will and Testament
3. Persistent Session

Keep Alive Interval (-k)
---------------------------------------------------------------------

BHIoT$ mosquitto_pub -t cdac/test -k 10 -h localhost -p 1883 -l -d
Client null sending CONNECT
Client null received CONNACK (0)
hi
Client null sending PUBLISH (d0, q0, r0, m1, 'cdac/test', ... (2 bytes))
Client null sending PINGREQ
Client null received PINGRESP
^C
------------------------------------------------------------------------
# Last Will and Testament (LWT)
 - In case publisher (IoT Device ) stop  sending the data due to network error
 - Subscriber receive the message on last will topic
-----------------------------------
# Pub --

mosquitto_pub \
-i desd \
-t cdac/desd/sensordata \
--qos 1 \
-r \
--will-qos 1 \
--will-topic cdac/desd/sensorissue \
--will-retain \
--will-payload "desd_device with UUID 3289 failed to send data due to unexpected error" \
-h localhost \
-p 1883 \
-l

# Subscriber for normal message

mosquitto_sub \
-t cdac/desd/sensordata \
-h localhost \
-p 1883

# Subscriber to receive Last will payload (in case of ungraceful disconnect)

mosquitto_sub \
-t cdac/desd/sensorissue \
-h localhost \
-p 1883


# Receive the normal and Last will payload on the same topic (Using the concept of wild card )
# Multiple ways has been demonstrated below
---------------------------------------
mosquitto_sub \
-t cdac/desd/+
-h localhost \
-p 1883


mosquitto_sub \
-t cdac/+/+
-h localhost \
-p 1883


mosquitto_sub \
-t cdac/#
-h localhost \
-p 1883

mosquitto_sub \
-t \#
-h localhost \
-p 1883
--------------------------------------------------------------

mosquitto_sub \
-t +/+/+
-h localhost \
-p 1883

----------------------
# Persistent session concept
 -  In case of subscriber get disconnected from the broker (broker maintains the published messages at broker)
 -  Only valid for QOS 1 and QOS 2
 -  client id is mandetory (i or -I )
 -  c flag is used to disable clean session (Enable Persistent session)  
-------------------------------------------------------------------------------

# Publish some sample payload (stdin line by line)

Publisher (client id amd QOS(1/2 is mandetory))

-c (to disable clean session hence enable the persistent session)

    mosquitto_pub \
    -i desd \
    -c \
    -t cdac/desd/humidity \
    --qos 1 \
    -h localhost \
    -p 1883 \
    -l

# Subscriber

mosquitto_sub -i desdsub -c -t cdac/desd/humidity -q 1 -h localhost -p 1883



