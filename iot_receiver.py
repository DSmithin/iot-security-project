import paho.mqtt.client as mqtt
import hmac, hashlib
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms

# ---------- Configuration ----------
BROKER = "test.mosquitto.org"
PORT = 1883
TOPIC = "iot/sensor"

key = b"12345678901234567890123456789012"
nonce = b"1234567890123456"
secret_key = b"supersecretkey"

# ---------- Functions ----------
def decrypt_message(ciphertext):
    cipher = Cipher(algorithms.ChaCha20(key, nonce), mode=None)
    decryptor = cipher.decryptor()
    return decryptor.update(bytes.fromhex(ciphertext)).decode()

def verify_hmac(message, received_hmac):
    expected = hmac.new(secret_key, message.encode(), hashlib.sha256).hexdigest()
    return hmac.compare_digest(expected, received_hmac)

# ---------- Callback ----------
def on_message(client, userdata, msg):
    try:
        payload = msg.payload.decode()

        if "|" not in payload:
            print("🚨 Invalid format!")
            return

        encrypted, received_hmac = payload.split("|")

        if not verify_hmac(encrypted, received_hmac):
            print("🚨 Tampered or fake message rejected!")
            return

        decrypted = decrypt_message(encrypted)
        print(f"✅ Decrypted: {decrypted}")

    except Exception as e:
        print(f"🚨 Error: {e}")

# ---------- MQTT ----------
client = mqtt.Client()
client.on_message = on_message

client.connect(BROKER, PORT, 60)
client.subscribe(TOPIC)

print("📡 Listening...")
client.loop_forever()