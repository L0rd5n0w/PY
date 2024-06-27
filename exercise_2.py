user_name = input(' Enter a username: ')
password = len(input(' Enter your preferred password: '))

secret = '*' * password
print(f' {user_name}, Your password "{secret}" is {password} characters long')

# PASSED