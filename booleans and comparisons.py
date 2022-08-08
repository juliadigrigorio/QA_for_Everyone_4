a=2
b=3
print(a==b)

x = 8
y = 6
if x > y:
    print('True')
else:
    print('False')


x = 3
y = 6
if x > y:
    print(f'{x} is greater than {y}')
else:
    print(f'{x} is less than {y}')


x = 0
y = 6
if (x == 0) or (y == 0):
    print('One or both numbers are not positive, can\'t proceed with the comparison!')
elif (x > 0) and (y > 0) and (x > y):
    print(f'{x} is greater than {y}')
elif (x > 0) and (y > 0) and (x < y):
    print(f'{x} is less than {y}')


op = 'ella'
print('*'.join(op))
op1 = "*".join(op)
char = op1.split('*')
print(char)
char.reverse()
print(char)
op3 = "".join(char)
if (op == op3):
    print("palindrome")
else:
    print("NOT palindrome")


