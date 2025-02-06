from twilio.rest import Client

account_sid = 'Account SID'
auth_token = 'Auth Token'

# https://console.twilio.com/?frameUrl=%2Fconsole%3Fx-target-region%3Dus1

client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+16203903227',
  body='안녕하세요 파이썬 문자 알람 테스트입니다.',
  to='+821027555836'
)

print(message.sid)
print("SUCCESS")