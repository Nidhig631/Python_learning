How to snd text msg from python code through Twilio Messaging?


Twilio Messaging is an API to send and receive SMS, MMS, OTT messages globally.
It uses intelligent sending features to ensure messages reliably reach 
end users wherever they are. 
Twilio has SMS-enabled phone numbers available in more than 180 countries.

-- To snd msg using python

step 1:- create a folder named Pytext and add app.py file

#install module twilio
pipenv install twilio 

# import client from twilio rest api
from twilio.rest import Client

step 2:- create  account on twilio and get Project Info(account_sid,auth_token)
         and generate phone number to snd text msg from twilio
account_sid = "..."
auth_token = "..."

step 3:- create config.py file and store account_sid and auth_token in config.py file.

step 4:- create .gitignore.py file 
 # add
 config.py
 
step 5:- open app.py and add these lines  
# to(whom to send msg)
# from (number generated from twilio)
import config
client = Client(config.account_sid, config.auth_token)
client.messages.create(to="....",
                       from_="....",
                       body="This is our first message")
