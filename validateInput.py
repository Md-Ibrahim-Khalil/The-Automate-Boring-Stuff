while True:
    print('Enter Your Age:')
    age = input()
    if age.isdecimal():
        break
    print('Please Enter a number for your age:')

while True:
    print('Select a new password(letters and numbers only):')
    password = input()
    if password.isalnum():
        break
    print('Passwords can only have letters and numbers!')
