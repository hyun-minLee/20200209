i = 0
sum=0
print("종료하려면 음수를 입력하시오.")              # 무한반복문은 조건식을 True로 하면 된다.
                                                  # 루프 탈출은 break를 사용하면 된다.
while True:                   
    x = input("성적을 입력하시오")
    x=int(x)
    if x < 0:
        break
    else:
        pass
    sum = sum+x
    i = i+1

str=("성적의 평균은 %s=" %sum/i)
print(str)
