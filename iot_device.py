import paho.mqtt.client as mqtt
import hmac, hashlib
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms
import time

# ---------- Configuration ----------
BROKER = "test.mosquitto.org"
PORT = 1883
TOPIC = "iot/sensor"

key = b"12345678901234567890123456789012"
nonce = b"1234567890123456"
secret_key = b"supersecretkey"

# ---------- Functions ----------
def encrypt_message(plaintext):
    cipher = Cipher(algorithms.ChaCha20(key, nonce), mode=None)
    encryptor = cipher.encryptor()
    return encryptor.update(plaintext.encode()).hex()

def generate_hmac(message):
    return hmac.new(secret_key, message.encode(), hashlib.sha256).hexdigest()

# ---------- MQTT ----------
client = mqtt.Client()
client.connect(BROKER, PORT, 60)

# ---------- Loop ----------
while True:
    data = "Temperature: 22C"
    encrypted = encrypt_message(data)
    signature = generate_hmac(encrypted)

    payload = f"{encrypted}|{signature}"
    client.publish(TOPIC, payload)

    print(f"📡 Sent: {payload}")
    time.sleep(5)