import random
import pandas as pd
import smtplib
from datetime import datetime
import os


MY_EMAIL = "Your Email"
PASSWORD = "Password"
print(PASSWORD)

data = pd.read_csv("birthdays.csv")

today = datetime.now()
today_tuple = (today.month, today.day)

birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthday_dict:
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        birthday_person = birthday_dict[today_tuple]
        contents = letter_file.read()
        message = contents.replace("[NAME]", birthday_person["name"])

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL, to_addrs=birthday_person["email"], msg=message)
    connection.close()
