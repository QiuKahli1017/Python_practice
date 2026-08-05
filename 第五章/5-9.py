name=input()
if name=='admin':
    print('Hello admin,would you like to see a status report?')
elif name=='':
    print('We need to find some users!')
else:
    print(f'Hello {name},thank you for logging in again')
