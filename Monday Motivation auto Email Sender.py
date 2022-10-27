import datetime as dt
import random
import smtplib

my_email = "test@gmail.com"
password= "passtest"


now = dt.datetime.now()
weekday = now.weekday()

if weekday == 0:
    with open("quotes.txt") as file:
        line = file.readlines()
        send_line = random.choice(line)
    print(send_line)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="test@yahoo.com",
                            msg=f"Subject:Monday Motivation\n\n {send_line}")


