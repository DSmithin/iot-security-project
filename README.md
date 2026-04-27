#  IoT Security Project

## Efficient Methods for Securing IoT Devices Against Cyberattacks

This project implements a lightweight and secure communication system for IoT devices using encryption and authentication.

---

##  Features

-  ChaCha20 encryption (confidentiality)
-  HMAC-SHA256 authentication (integrity)
-  MQTT communication protocol
-  Protection against tampered or fake messages

---

##  Architecture

IoT Device (Sender) → MQTT Broker → Receiver

- Sender encrypts and signs data
- Receiver verifies and decrypts
- Invalid messages are rejected

---

##  Testing

| Test Case | Result |
|----------|--------|
| Valid message | ✅ Accepted |
| Tampered message | ❌ Rejected |
| Fake HMAC | ❌ Rejected |

---

## ▶ How to Run

###  Install Dependencies
Make sure Python is installed, then run:

pip install -r requirements.txt

---

###  Run the Receiver (Listener)
Open a terminal and start the receiver:

python iot_receiver.py

You should see:
📡 Listening...

---

###  Run the Sender (IoT Device)
Open a second terminal and run:

python iot_device.py

You will see encrypted messages being sent:
📡 Sent: <encrypted_data>|<hmac>

---

###  Observe Secure Communication
In the receiver terminal, you should see:

✅ Decrypted: Temperature: 22C

This confirms that:
- Data is encrypted before transmission
- Message integrity is verified using HMAC

---

###  Simulate an Attack (Optional)
Open a third terminal and run:

python attacker.py

The receiver will reject the fake message:

🚨 Tampered or fake message rejected!

---

##  What This Demonstrates
- Secure communication using lightweight encryption (ChaCha20)
- Message integrity verification with HMAC-SHA256
- Protection against tampering and unauthorized message injection

---

##  Notes
- Uses a public MQTT broker: test.mosquitto.org
- Internet connection is required
- Run sender and receiver at the same time for proper operation