from bs4 import BeautifulSoup
import requests
import smtplib
import threading
import datetime as dt

GMAIL_SERVER = "smtp.gmail.com"
MY_EMAIL = "david822.mex@gmail.com"
PASSWORD = "Guapo822."
TO_EMAIL = "tianchuan87822@hotmail.com"


def check_availability():
    send_email = False
    body = ""
    messages = []

    # Things to scrape:
    tasks = [
        {
            "product": "Mac mini",
            "URL": "https://www.apple.com/mx/shop/buy-mac/mac-mini",
            "name": "button",
            "class": "button button-block disabled",
        },
        {
            "product": "IKEA LACK",
            "URL": "https://www.ikea.com/mx/es/p/lack-mesa-de-centro-efecto-roble-tinte-blanco-50319029/",
            "name": "button",
            "class": "range-revamp-btn--full-width",
        }
    ]
    for task in tasks:
        # scraping webpage:
        res = requests.get(task["URL"])
        page = res.text
        soup = BeautifulSoup(page, "html.parser")
        result = soup.find(name=task["name"], class_=task["class"])
        if result is None:
            send_email = True
            message = task['product'] + ": " + task['URL']
            messages.append(message)

    # Loop through all messages:
    if len(messages) > 0:
        for msg in messages:
            body += msg + "\n\n"

    # send email
    # IMPORTANT: Computer name can't be chinese. MSG can't include emojis.
    if send_email:

        subject = "Something became available."
        email_msg = f"Subject:{subject}\n\n{body}"

        with smtplib.SMTP(GMAIL_SERVER) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, PASSWORD)
            connection.sendmail(MY_EMAIL, MY_EMAIL, email_msg)
    else:
        print("Nothing is available yet. " + str(dt.datetime.now()))

    # run every hour.
    threading.Timer(3600, check_availability).start()


# Finally run the program
check_availability()
