# 🛰️ ISS Overhead Notifier

A Python automation script that tracks the position of the International Space Station (ISS) in real-time. It sends you an email notification when the ISS is overhead and visible (at night).

## 🌟 Features

* **Real-time Tracking:** Uses the Open Notify API to get the live latitude and longitude of the ISS.
* **Day/Night Cycle:** Uses the Sunrise-Sunset API to determine if it is currently dark at your location (the ISS is only visible against a dark sky).
* **Email Alerts:** Automatically sends an email via SMTP when the ISS is within your range and the sky is dark.
* **Background Execution:** The script runs indefinitely, checking conditions every 60 seconds.

## 📂 Project Structure

* **`main.py`**: The primary script containing the logic for API calls and email sending.
* **`config.py`**: A separate file (usually git-ignored) to store sensitive credentials like your email and app password.

## 🛠️ Prerequisites & Setup

### 1. Install Dependencies
This project uses the `requests` library to fetch API data.
```bash
pip install requests
# config.py
my_email = "your_email@gmail.com"
my_password = "your_app_password" # Use a Google App Password, not your login password