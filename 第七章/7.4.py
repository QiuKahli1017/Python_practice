pizza=''
while True:
    text0=input('Fill in the toppings:')
    if text0==('quit'):
        break
    else:
        pizza+=text0
        pizza+=' '
print(pizza)