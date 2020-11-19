import smtplib

GMAIL_SERVER = "smtp.gmail.com"
MY_EMAIL = "david822.mex@gmail.com"
PASSWORD = " "
TO_EMAIL = "tianchuan87822@hotmail.com"
SUBJECT = "This is a test from Python."
BODY = "Hello from Python."
MSG = f"Subject:{SUBJECT}\n\n{BODY}"


with smtplib.SMTP(GMAIL_SERVER) as connection:
    connection.starttls()
    connection.login(MY_EMAIL, PASSWORD)
    connection.sendmail(MY_EMAIL, TO_EMAIL, MSG)


# IMPORTANT: Computer name can't be chinese. MSG can't include emojis.
