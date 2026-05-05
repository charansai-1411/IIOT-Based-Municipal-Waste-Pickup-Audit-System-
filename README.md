# 🚛 IoT-Based Municipal Waste Pickup Confirmation System

## 📌 Overview

This project is an **IoT-based waste collection monitoring system** designed to improve transparency and accountability in municipal waste management.

The system uses **RFID technology with Raspberry Pi** to detect waste collection events and logs them to the cloud (**ThingSpeak**) for real-time monitoring and auditing.

---

## 🎯 Problem Statement

Municipal waste collection systems often lack:

* Real-time monitoring
* Digital verification of pickups
* Transparency in operations

Manual reporting can lead to:

* Missed pickups
* False reporting
* Lack of accountability

---

## 💡 Solution

This project provides an automated system that:

1. Detects waste collection using RFID
2. Processes data using Raspberry Pi
3. Sends data to ThingSpeak cloud
4. Stores records for monitoring and audit

---

## 🛠️ Technologies Used

* **Raspberry Pi**
* **RFID (MFRC522)**
* **Python**
* **ThingSpeak Cloud**
* **SPI Communication**

---

## 🔌 Hardware Components

* Raspberry Pi
* RFID Reader (RC522)
* RFID Tags
* Power Supply
* Physitech IoT Trainer Board

---

### Workflow:

1. RFID tag is placed at waste collection point
2. Worker scans RFID using reader
3. Raspberry Pi detects the card
4. System logs the event
5. Data is uploaded to ThingSpeak
6. Dashboard displays pickup confirmation

---


## ☁️ ThingSpeak Configuration

Create a channel with fields:

| Field   | Description   |
| ------- | ------------- |
| Field 1 | RFID ID       |
| Field 2 | Location ID   |
| Field 3 | Timestamp     |
| Field 4 | Pickup Status |

---

## ▶️ How to Run

1. Enable SPI:

```bash
sudo raspi-config
```

2. Install dependencies:

```bash
pip3 install mfrc522 requests
```

3. Run the code:

```bash
sudo python3 main.py
```

4. Scan RFID card

---

## 📊 Output

* Console shows detection
* Data uploaded to ThingSpeak
* Graph updates in real-time

---

## ⚠️ Notes

* UID is used for stable operation
* ThingSpeak requires 15-second delay between updates
* Ensure internet connection is active

---

## 🚀 Future Enhancements

* GPS integration for live tracking
* Camera verification
* Mobile app dashboard
* Real RFID UID mapping
* Alert system for missed pickups

---

## 🎓 Conclusion

This system provides a **reliable, low-cost IoT solution** for waste management by ensuring:

* Transparency
* Accountability
* Real-time monitoring

---

## 👨‍💻 Authors

* Charan Sai
* Shreeya

---
