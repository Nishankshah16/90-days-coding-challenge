from twilio.rest import Client
from dotenv import load_dotenv
import smtplib
import os

load_dotenv()

class NotificationManager:
    def __init__(self):
        # twilio credentials
        self.account_sid = os.environ["TWILIO_ACC_SID"]
        self.auth_token = os.environ["TWILIO_AUTH_TOKEN"]
        # gmail credentials
        self.my_email = os.environ["SMTP_EMAIL"]
        self.my_password = os.environ["SMTP_PASS"]
        self.client = Client(self.account_sid, self.auth_token)
        self.connection =  smtplib.SMTP(os.environ["SMTP_PROVIDER"], port=587)

    def send_msg(self, msg_body):
        message = self.client.messages.create(
        body=msg_body, 
        from_= os.environ["TWILIO_VIRTUAL_NUMBER"],  
        to= os.environ["TWILIO_VERIFIED_NUMBER"]
        )

        print(message.status)

    def send_mail(self, email, msg_body):
        try:
          with self.connection:
            self.connection.starttls()
            self.connection.login(user=self.my_email,password=self.my_password)
            for mail in email:
                self.connection.sendmail(from_addr=self.my_email,to_addrs=mail,msg=f"Subject: Flight Club \n\n{msg_body}".encode('utf-8'))

        except smtplib.SMTPException as e:
            print(f"SMTP error occurred: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")