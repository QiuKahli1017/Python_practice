print('The pastrami is gone out')
sandwich_orders=['fish','meat','lamb','pastrami','pastrami','pastrami']
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(f'We only have:{sandwich_orders}')