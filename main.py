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
expression = input('Enter a mathematical expression: ')
result = eval(expression)
print('Result:', result)

if expression == 1:
    result = add(a,b,c)
    print('Result:', result)
elif expression == 2:
    result = sub(a,b,c)
    print('Result:', result)
elif expression == 3:
    result = mul(a,b,c)
    print('Result:', result)
elif expression == 3:
    result = div(a,b,c)
    print('Result:', result)

