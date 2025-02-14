# ISS Tracker 🚀

## Overview

ISS Tracker is a simple Python project that tracks the location of the International Space Station (ISS) and notifies you if it is overhead during nighttime. The project uses the `requests` module to fetch the ISS location and the sunrise/sunset times, and `smtplib` to send an email alert when the conditions are met.

---

## Features ✨
- Tracks the real-time position of the ISS.
- Checks if the ISS is within ±5 degrees of your location (latitude and longitude).
- Uses sunrise and sunset times to determine if it's nighttime.
- Sends an email notification when the ISS is overhead at night.

---

## How It Works 🛠️
1. The program fetches the ISS's current latitude and longitude from the `http://api.open-notify.org/iss-now.json` API.
2. It fetches sunrise and sunset times for your location using the `https://api.sunrise-sunset.org/json` API.
3. If the ISS is overhead (within ±5 degrees of your location) and it is nighttime, an email is sent with the subject "Look up! The ISS is above your head."

---

## Installation 🧑‍💻

1. Clone this repository or download the source code.
2. Ensure you have Python 3 installed.
3. Install the necessary dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Configuration ⚙️

Edit the `config.py` or main configuration section to set:
- Your latitude and longitude.
- Your email address.
- Your email password (use an app password if using Gmail).

---

## Running the Project 🚀

Run the program:
```bash
python main.py
```
The program will check every minute if the conditions are met and send an email notification if the ISS is overhead.

---
