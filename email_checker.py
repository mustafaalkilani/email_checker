import requests,sys

email_address = str(sys.argv[1])
response = requests.get(
    "https://isitarealemail.com/api/email/validate",
    params = {'email': email_address})

status = response.json()['status']
if status == "valid":
  print(f"email: '{email_address}' is valid")
  validemail = open('outputEmails/validemails.txt',mode='a')
  validemail.write(f'email: "{email_address}" is valid\n')
  validemail.close()
elif status == "invalid":
  print(f"email: '{email_address}' is invalid")
  invalidemail = open('outputEmails/invalidemails.txt', mode='a')
  invalidemail.write(f'email: "{email_address}" is invalid\n')
  invalidemail.close()
else:
  print(f"email: '{email_address}' was unknown")
  unknownemail = open('outputEmails/unknownemails.txt',mode='a')
  unknownemail.write(f'email: "{email_address}" was unknown\n')
  unknownemail.close()
