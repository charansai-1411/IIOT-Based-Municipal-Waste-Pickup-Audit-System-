import time
import requests
import RPi.GPIO as GPIO
from mfrc522 import MFRC522

GPIO.setmode(GPIO.BCM)

reader = MFRC522()

# ThingSpeak config
THINGSPEAK_API_KEY = "YOUR_API_KEY"
THINGSPEAK_URL = "https://api.thingspeak.com/update"

# Dummy UID (fixed for demo)
DUMMY_UID = 12345678

def send_to_thingspeak(tag_id):
    payload = {
        'api_key': THINGSPEAK_API_KEY,
        'field1': tag_id,
        'field2': 1,                  # location ID
        'field3': int(time.time()),   # timestamp
        'field4': 1                   # status
    }

    try:
        response = requests.get(THINGSPEAK_URL, params=payload)
        print("📡 Response:", response.text)
    except Exception as e:
        print("❌ Error:", e)

print("🚛 Waste Pickup System Ready")
print("Scan RFID Card...")

try:
    while True:
        (status, TagType) = reader.MFRC522_Request(reader.PICC_REQIDL)

        if status == reader.MI_OK:
            print("\n📡 Card detected")

            # Use dummy UID instead of real UID
            tag_id = DUMMY_UID

            print("⚠️ Using Dummy UID:", tag_id)

            # Send to ThingSpeak
            send_to_thingspeak(tag_id)

            print("📤 Data sent successfully")

            # IMPORTANT: ThingSpeak delay
            time.sleep(15)

        else:
            print("Waiting for card...")
            time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()
    print("Stopped")
