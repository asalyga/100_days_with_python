import datetime as dt
import pandas as pd
from random import choice
import smtplib

today_date = dt.datetime.now()
today = (today_date.month, today_date.day)
data = pd.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
my_email = "ur email here"
password = "ur password here"

if today in birthdays_dict:
    person = birthdays_dict[today]
    letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
    random_letter = choice(letters)
    file_path = f"letter_templates/{random_letter}"
    with open(file_path) as letter_file:
        content = letter_file.read()
        ready_letter = content.replace("[NAME]", person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=person["email"],
                            msg=f"Subject:Birthday Wishes \n\n{ready_letter}")
        connection.close()
