

x = 23
epsilon = 0.0001
step = 0.0001
guess = 0.0

while abs(guess**2 - x) >= epsilon:
    if guess >= x:
        break
    else:
        guess += step

if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))
