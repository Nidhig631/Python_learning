# import client from twilio rest api
from twilio.rest import Client
import config

client = Client(config.account_sid, config.auth_token)
message_info = client.messages.create(to="+91 9560925869",
                                      from_="+12244790803",
                                      body="This is our first message")
print(message_info)
