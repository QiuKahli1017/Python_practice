current_users=['Abe','Tax','John','Max','Nico']
new_users=['Tom','Cxy','KK','Nico',"MAX"]
new_users=new_users.title()
for new_user in new_users:
    if new_user.title() in current_users:
        print(new_user,',Please use another name')
    else:
        print("True")
