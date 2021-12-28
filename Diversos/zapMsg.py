from twilio.rest import TwilioRestClient
import twilio
print twilio.__version__
# Your Account SID from twilio.com/console
account_sid = "AC6791725bc93116fbd42b4cd477996f7d"
# Your Auth Token from twilio.com/console
auth_token  = "30ed212f6a2bbc05d103b67426b8509a"

client = TwilioRestClient(account_sid, auth_token)

message = client.sms.messages.create(
    body="Sent from your Twilio trial account - hello from python",
    to="my number phone goes here",
    from_="+14695356845" )

print message.sid