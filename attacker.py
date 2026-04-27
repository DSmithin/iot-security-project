import paho.mqtt.client as mqtt

BROKER = "test.mosquitto.org"
PORT = 1883
TOPIC = "iot/sensor"

client = mqtt.Client()
client.connect(BROKER, PORT, 60)

# Fake message (no encryption, invalid HMAC)
fake_payload = "Temperature: 999C|fakehmac123"

client.publish(TOPIC, fake_payload)
print("🚨 Fake message sent!")