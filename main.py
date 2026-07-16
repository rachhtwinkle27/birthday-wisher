import random
import pandas
import smtplib
from datetime import datetime
import os

MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

today = dt.datetime.now()
today_tuple = (today.month, today.day)

data_file = pandas.read_csv("birthdays.csv")

birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data_file.iterrows()}

if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]

    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"

    with open(file_path) as file:
        letter_content = file.read()

        letter_content = letter_content.replace("[NAME]", birthday_person["name"])

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=test_email, password=test_password)
            connection.sendmail(
                from_addr=test_email,
                to_addrs=birthday_person["email"],
                msg=f"Subject:Happy Birthday!\n\n{letter_content}"
            )

    print("Birthday email sent successfully")
else:
    print("No birthdays today")
