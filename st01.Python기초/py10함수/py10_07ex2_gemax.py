def getmax(x,y):
    if(x>y):
        return x
    else:
        return y


def myinput():
    value=int(input("정수의값을 입력하시오"))
    return value

value1=myinput()
value2=myinput()

result=getmax(value1,value2)
print("두개의 입력받은 정수중 큰값은 %d" %result)

def main():
    value=int(input("정수의값을 입력하시오"))
    return value

value1=myinput()
value2=myinput()

result=getmax(value1,value2)
print("두개의 입력받은 정수중 큰값은 %d" %result)
