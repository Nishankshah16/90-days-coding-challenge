from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
from dotenv import load_dotenv
import os

load_dotenv()

# twilio credentials
account_sid = os.environ["TWILIO_ACC_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]

class NotificationManager:
    def __init__(self):
        self.client = Client(account_sid, auth_token)
    def send_msg(self, msg_body):
        message = self.client.messages.create(
        body=msg_body, 
        from_= os.environ["TWILIO_VIRTUAL_NUMBER"],  
        to= os.environ["TWILIO_VERIFIED_NUMBER"]
        )

        print(message.status)