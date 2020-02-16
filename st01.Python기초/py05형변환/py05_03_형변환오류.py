
# 숫자가 아닌 것을 정수로 변환하려고 할 때

# 숫자가 아닌 것을 실수로 변환 할 때

# 소수점이 있는 숫자 형식의 문자열을 int() 함수로 변환 할 때

try:
    i =int("안녕하세요")
    print(i)
except ValueError:
    pass
    #print("숫자가 아닙니다. 다시입력하시오.")

try:
    e=str("안녕하세요")
    print(e)
except ValueError:
    print("숫자가 아닙니다. 다시입력하시오.")

try:
    f=input("값을 입력하세요.")
    if f ==type(int)
        print(f)
    else:
        print("잘못된값입니다.")
except ValueError:
    print("숫자가 아닙니다. 다시입력하시오.")