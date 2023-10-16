def add(a,b,c):
    return a + b - c

def sub(a,b,c):
    return a - b + c

def mul(a,b,c):
    return a * b - c

def div(a,b,c):
    return a / b * c

a = int(input('input a number'))
b = int(input('input a number'))
c = int(input('input a number'))

print('select an operation:')
print('1. add')
print('2. sub')
print('3. mul')
print('4. div')
choice = int(input('input operations choice btw (1-4):'))
while choice != 1 and choice != 2 and choice != 3 and choice != 4:
    print('Error please enter a valid choice.')
    choice = int(input('input operation choice btw (1-4):'))
if choice == 1:
    result = add(a,b,c)
    print('Result:', result)
elif choice == 2:
    result = sub(a,b,c)
    print('Result:', result)
elif choice == 3:
    result = mul(a,b,c)
    print('Result:', result)
elif choice == 3:
    result = div(a,b,c)
    print('Result:', result)

else:
    print('invalid input')