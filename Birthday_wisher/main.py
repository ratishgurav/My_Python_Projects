##################### Extra Hard Starting Project ######################
import pandas as pd
import datetime as dt
import random
import smtplib
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

load_dotenv()


## Getting the details
details=pd.read_csv("birthdays.csv")
details_dict=details.to_dict(orient="records")
print(details_dict)

## Get the letter
now=dt.datetime.now()
letter_template=[]
with open("letter_templates/letter_1.txt") as l1:
    l1=l1.read()
    letter_template.append(l1)
with open("letter_templates/letter_2.txt") as l2:
    l2=l2.read()
    letter_template.append(l2)
with open("letter_templates/letter_3.txt") as l3:
    l3=l3.read()
    letter_template.append(l3)
print(letter_template)

## Checking and sending the letter to the email
letter=""
my_email = os.getenv("my_email")
my_password = os.getenv("my_password")
for i in details_dict:
    if i['month']==now.month and i['day']==now.day:
        letter=random.choice(letter_template)
        final_letter=letter.replace("[NAME]",i['name'])
        email=i['email']
        # with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        #     connection.starttls()
        #     connection.login(user=my_email,password=my_password)
        #     connection.sendmail(from_addr=my_email,
        #                         to_addrs=email,
        #                         msg=f"Subject:HAPPY BIRTHDAY!!\n\n{final_letter}")
        # Prepare email message with correct encoding
        msg = MIMEText(final_letter, _charset='utf-8')
        msg['Subject'] = "HAPPY BIRTHDAY🥳🎉!!"

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=email,
                msg=msg.as_string()  # Properly formatted message with headers
            )





