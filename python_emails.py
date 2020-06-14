import csv
import ssl
import smtplib

message = """\

From: {sender}
To: {email}
Subject: Your Grades

Hi {name} your grade is {grade}

"""
smtp_server = 'smtp.gmail.com'
port = 465


sender = 'fastklapsylan@gmail.com'
password = input("Enter your password: ")


context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
    server.login(sender, password)
    with open('contacts.csv') as file:
        reader = csv.reader(file)
        next(reader)
        for name, email, grade in reader:
            server.sendmail(
                sender,
                email,
                message.format(
                    sender=sender,
                    email=email,
                    name=name,
                    grade=grade
                )
            )
