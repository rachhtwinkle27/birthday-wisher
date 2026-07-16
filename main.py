import random
import pandas
import smtplib
import datetime as dt

test_email = "testing.python5394@gmail.com"
test_password = "lemkrwrghzfycjdh"


# ---------------------- Current date ------------------------#
today = dt.datetime.now()
today_tuple = (today.month, today.day)

# ------------------------ Read CSV ------------------------#

data_file = pandas.read_csv("birthdays.csv")

# ------------------------ Dictionary comprehension to create dictionary from birthdays.csv ------------------#

birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data_file.iterrows()}

# ------------------------------- Check if today's month/day tuple matches one of the key in birthdays.csv-------------#

if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]

    # ------------------------- Random letters ---------------------#

    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"

    # ----------------------- Read letters ---------------------- #

    with open(file_path) as file:
        letter_content = file.read()

        # -------------------- Replace name --------------------- #

        letter_content = letter_content.replace("[NAME]", birthday_person["name"])

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=test_email, password=test_password)
            connection.sendmail(
                from_addr=test_email,
                to_addrs=birthday_person["email"],
                msg=f"Subject:Happy Birthday!\n\n{letter_content}"
            )

    print("Mail sent")
