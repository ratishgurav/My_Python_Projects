# ☔ Rain Alert SMS Notifier

A Python automation script that checks the weather forecast and sends an SMS alert if rain is expected. This project is optimized to run on **PythonAnywhere** using a proxy server for the Twilio API.

## 🌟 Features

* **Forecast Monitoring:** Queries the OpenWeatherMap API for the upcoming forecast.
* **Rain Detection:** Analyzes weather condition codes to determine if precipitation is likely (codes < 700).
* **SMS Alerts:** Uses the Twilio API to send a text message reminder to bring an umbrella.
* **PythonAnywhere Ready:** configured with a `TwilioHttpClient` proxy to bypass free-tier restrictions on PythonAnywhere.

## 🛠️ Prerequisites

* **Python 3.x**
* **OpenWeatherMap API Key:** Sign up at [openweathermap.org](https://openweathermap.org/api) to get a free key.
* **Twilio Account:** Sign up at [twilio.com](https://www.twilio.com) to get an Account SID, Auth Token, and a virtual phone number.

### Dependencies
Install the required libraries:
```bash
pip install requests twilio

export OWM_API_KEY="your_owm_api_key"
export AUTH_TOKEN="your_twilio_auth_token"

export OWM_API_KEY=your_actual_key; export AUTH_TOKEN=your_actual_token; python3 main.py