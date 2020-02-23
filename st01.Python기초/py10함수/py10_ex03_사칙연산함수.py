def Add(x, y):
    result = x+y
    return result

def Minus(x, y):
    result = x-y
    return result

def Mul(x, y):
    result = x*y
    return result

def Div(x, y):
    try:
        result = x/y

    except ZeroDivisionError as ex:
        print("0으로 나누면안됩니다", ex)
    return result


x = int(input("첫번째 값을 입력하시오"))
y = int(input("두번째 값을 입력하시오"))



value1 = Add(x, y)
value2 = Minus(x, y)
value3 = Mul(x, y)
value4 = Div(x, y)

print(value1)
print(value2)
print(value3)
print(value4)
