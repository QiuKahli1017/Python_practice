sandwich_orders=['fish','meat','lamb']
finished_sandwiches=[]
while sandwich_orders:
    sandwich=sandwich_orders.pop()
    print(f'I made a {sandwich} sandwich')
    finished_sandwiches.append(sandwich)
print('The sandwich on the order are:')
print(finished_sandwiches)