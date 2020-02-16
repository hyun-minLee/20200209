# 문자열을 입력 받고 숫자인지 문자인지 판별하는 프로그램을 작성하시오.


text=input("숫자나 문자를 입력하시오.")

if ("a" <=chr(text) <="z") or ("A"<=chr(text) <="Z"):
    print("영문자입니다")
else:
    print("숫자입니다")

