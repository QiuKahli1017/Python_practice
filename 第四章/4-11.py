my_pizza=['G','T']
f_pizza=my_pizza[:]
my_pizza.append('A')
f_pizza.append('D')
print(my_pizza,end=' ')
for i in my_pizza:
    print(i,end=' ')

print(f_pizza,' ')
for i in f_pizza:
    print(i,end=' ')
