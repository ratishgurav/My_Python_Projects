# 🎂 Automated Birthday Wisher

A Python automation script that tracks birthdays and automatically sends a personalized email greeting when the date matches. It uses randomized letter templates to keep messages unique and manages security credentials using environment variables.

## 📂 Project Structure

* **`main.py`**: The core script. It checks today's date against the CSV data, picks a random letter, replaces the placeholders, and sends the email.
* **`birthdays.csv`**: A database file containing names, emails, and birth dates (year, month, day).
* **`letter_templates/`**: A folder containing different text files (e.g., `letter_1.txt`, `letter_2.txt`) used as message templates.
* **`.env`**: A local configuration file for storing your email credentials securely (this file is gitignored and not shared).

## 🛠️ Prerequisites

* Python 3.x
* A Gmail account (or other SMTP provider).
* **Libraries:** You may need `pandas` (for reading the CSV) and `python-dotenv` (to read the .env file).

```bash
pip install pandas python-dotenv

MY_EMAIL=your_email@gmail.com
MY_PASSWORD=your_app_password