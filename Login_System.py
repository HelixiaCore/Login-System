# My First Project is Login System since is 9/8/2026

correct_username = 'admin'
correct_password = '@abc'
max_attempt = 3

for attempt in range(max_attempt):
    username = input("please enter username: ")
    password = input("please enter password: ")
    if username == correct_username and password == correct_password:
        print(f"\nPerson is found with {correct_username} is name and {correct_password} is password")
        break
    else:
        print("This information is wrong! please try again")
else:
    print("\n\nsorry! This acount is locked...!")