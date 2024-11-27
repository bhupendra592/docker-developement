import paho.mqtt.client as mqtt
import logging
import signal
import sys
import os
import time

# Environment variables for configuration
BROKER = os.getenv("BROKER", "localhost")
PORT = int(os.getenv("PORT", 1883))
TOPIC = os.getenv("TOPIC", "sensor/data")

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Define the MQTT client globally
client = mqtt.Client()

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        logger.info("Connected successfully to broker")
        client.subscribe(TOPIC, qos=1)
        logger.info(f"Subscribed to {TOPIC} with QoS 1")
    else:
        logger.error(f"Connection failed with code {rc}")

def on_message(client, userdata, msg):
    try:
        logger.info(f"Received message: {msg.payload.decode()} on topic {msg.topic}")
    except Exception as e:
        logger.error(f"Error processing message: {e}")

def on_disconnect(client, userdata, rc):
    if rc == mqtt.MQTT_ERR_SUCCESS:
        logger.info("Disconnected gracefully.")
    else:
        logger.warning(f"Disconnected unexpectedly (code {rc}). Attempting to reconnect...")
        reconnect_with_retry()

def reconnect_with_retry():
    retries = 5
    for attempt in range(retries):
        try:
            client.reconnect()
            return
        except Exception as e:
            logger.error(f"Reconnect attempt {attempt + 1}/{retries} failed: {e}")
            time.sleep(5)
    logger.critical("Failed to reconnect after multiple attempts. Exiting.")
    sys.exit(1)

def signal_handler(sig, frame):
    logger.info("Exiting subscriber gracefully...")
    client.disconnect()
    sys.exit(0)

def start_subscriber():
    client.on_connect = on_connect
    client.on_message = on_message
    client.on_disconnect = on_disconnect  # Assign disconnect callback

    try:
        client.connect(BROKER, PORT, 60)
    except Exception as e:
        logger.error(f"Failed to connect to broker: {e}")
        sys.exit(1)

    signal.signal(signal.SIGINT, signal_handler)
    client.loop_forever()

if __name__ == "__main__":
    start_subscriber()
