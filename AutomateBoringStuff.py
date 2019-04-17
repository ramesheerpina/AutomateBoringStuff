while True:
    print("Who are you?")
    name = input()
    if name != 'Joe':
        continue
    print("Hello, Joe, What is the password")
    print("What is your password")
    password = input()
    if password == 'fish':
        break
print("Granted")
