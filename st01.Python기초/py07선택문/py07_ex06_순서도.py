in_data=input("문자를입력하시오")

lenth=len(in_data)
print(lenth)

while lenth <3:
    print("문자열 길이가 짧습니다")
    in_data=input("문자를 다시입력하시오.")
    lenth2=len(in_data)
    if lenth2 >3:
        break
print("종료합니다.")



