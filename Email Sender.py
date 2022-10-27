
import smtplib
my_email = "test@gmail.com"
password= "passtest"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user= my_email, password= password)
    connection.sendmail(from_addr= my_email,
                        to_addrs="test@yahoo.com", 
                        msg="Subject:Hello\n\n This is the body")
