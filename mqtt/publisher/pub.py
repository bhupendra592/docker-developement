import os
import time
import random
import paho.mqtt.client as mqtt
import signal
import sys
import json
import logging
from datetime import datetime

BROKER = os.getenv("BROKER", "localhost")
PORT = int(os.getenv("PORT", 1883))
TOPIC = os.getenv("TOPIC", "sensor/data")

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

client = mqtt.Client()

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        logger.info("Connected successfully to broker")
    else:
        logger.error(f"Connection failed with code {rc}")

def signal_handler(sig, frame):
    logger.info("Exiting publisher gracefully...")
    client.disconnect()
    sys.exit(0)

def connect_with_retry():
    retries = 5
    for attempt in range(retries):
        try:
            client.connect(BROKER, PORT, 60)
            return
        except Exception as e:
            logger.error(f"Connection failed (Attempt {attempt + 1}/{retries}): {e}")
            time.sleep(5)
    logger.critical("Failed to connect after multiple attempts. Exiting.")
    sys.exit(1)

def generate_sensor_data():
    temperature = round(random.uniform(20.0, 30.0), 2)
    humidity = round(random.uniform(40.0, 60.0), 2)
    return {
        "temperature": temperature,
        "humidity": humidity,
        "timestamp": datetime.utcnow().isoformat()
    }

def publish_message():
    client.on_connect = on_connect
    connect_with_retry()

    while True:
        try:
            sensor_data = generate_sensor_data()
            payload = json.dumps(sensor_data)
            client.publish(TOPIC, payload, qos=1)
            logger.info(f"Published: {payload}")
            time.sleep(10)
        except KeyboardInterrupt:
            signal_handler(None, None)
        except Exception as e:
            logger.error(f"Error during publishing: {e}")

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    publish_message()
