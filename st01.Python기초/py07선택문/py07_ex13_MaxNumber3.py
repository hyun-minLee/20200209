a=int(input("첫번째값"))
b=int(input("두번째값"))
c=int(input("세번째값"))

if a>b:

    #a와 c를 비교한다
    if a>c:
        print("a가 가장크다")
    else:
        print("c가 가장크다")
else: 
     #b와 c를 비교한다
    if b>c:
        print("b가 가장크다")
    else:  #c>b>a
        print("c가 가장크다")
