import email.utils
import re
n = int(input())

for i in range(0, n):
    inpu = str(input())
    out = email.utils.parseaddr(inpu)
    #print(out)
    parsed_email_address = email.utils.formataddr(out)
    #print(parsed_email_address)
    if parsed_email_address == '':
        continue
    else:
        emai = parsed_email_address.split(' <')[1]
        emai = emai.replace('>', ' ')
        
    #print(emai)
    if emai == []:
        continue
    else:
        regexed = re.findall(r"^[a-zA-Z0-9]+[_-][a-zA-Z0-9]+[@][a-zA-Z]+[.][a-zA-z{1,3}]+", emai)
    #regexed[i].replace(r'[', '').replace(r"']", '')
    for i in regexed:
        print(i)
