import random
names = ['Steve','Albert','Coke','Tim']
message='I want to invite'+'\n'+names[0]+'\n'+names[1]+'\n'+names[2]+'\n'+names[3]
print(message)
person = names[2]
print(names)
del names[2]
names.append('Zhengning')
message='I want to invite'+'\n'+names[0]+'\n'+names[1]+'\n'+names[2]+'\n'+names[3]
print(message)

print('I found a much bigger table')
names.insert(0,'Alex')
names.insert(2,'Falcon')
names.append('Nico')
message=message='I want to invite'+'\n'+names[0]+'\n'+names[1]+'\n'+names[2]+'\n'+names[3]+'\n'+names[4]+'\n'+names[5]+'\n'+names[6]
print(message)
poped=names.pop(0)
print('Sorry '+poped+",the table isn't ready.")
poped=names.pop(0)
print('Sorry '+poped+",the table isn't ready.")
poped=names.pop(0)
print('Sorry '+poped+",the table isn't ready.")
poped=names.pop(0)
print('Sorry '+poped+",the table isn't ready.")
poped=names.pop(0)
print('Sorry '+poped+",the table isn't ready.")
message = "Hello "+names[0]+','+names[1]+",you are invited."
print(message)