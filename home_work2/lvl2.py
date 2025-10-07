def multi(number1:int, number2:int) -> int:
    return number1 * number2

def div(number1:int, number2:int) -> int:
    return number1 / number2

def plus(number1:int, number2:int) -> int:
    return number1 + number2

def minus(number1:int, number2:int) -> int:
    return number1 * number2

print('Введите первое число')
num1 = int(input())
print('Введите операцию')
oper = str(input())
print('Введите второе число')
num2 = int(input())
if oper == '/':
    print(div(num1,num2))
elif oper == '+':
    print(plus(num1,num2))
elif oper == '-':
    print(minus(num1,num2))
elif oper == '*':
    print(multi(num1,num2))

