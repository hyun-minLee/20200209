# 자동 판매기를 시뮬레이션하는 프로그램을 작성하여 보자. 
# 사용자는 1000원짜리 지폐와 500원짜리 동전, 100원짜리 동전을 사용할 수 있다. 
# 물건값을 입력하고 1000원권, 500원짜리 동전, 100원짜리 동전의 개수를 입력하면 
# 거스름돈을 계산하여서 동전으로 반환한다. 



# 거스름돈(500원 동전 개수)을 계산한다. 

# 거스름돈(100원 동전 개수)을 계산한다. 

# 거스름돈(10원 동전 개수)을 계산한다. 

# 거스름돈(1원 동전 개수)을 계산한다. 

# 출력


x=int(input("물건값을 입력하시오."))
a=int(input("천원권 매수를 입력하시오."))
b=int(input("500원자리 동전 갯수를 입력하시오"))
c=int(input("100원짜리 동전 갯수를 입력하시오"))

total = 1000*a   #250
total1= 500*b
total2= 100*c
total3=total+total1+total2
total4=total3-x
print("거스름돈", total4)

if total4 >=1000:
    print("천원짜리 받는갯수", total4 // 1000)
    total4=total4-(total4 % 1000)
    print(total4-(total4 % 1000))

if  500 <= total4 <1000:
    print("오백원짜리 받는갯수", total4 // 500)
    total4=total4 -(total4 % 500)
    print(total4)
    
if 100<= total4 < 500:
    print("백원짜리 받는갯수", total4 // 100)

#print("천원짜리 받는갯수", total4 // 1000)
#print("500원짜리 받는갯수", total4 //500)
#print("100원짜리 받는갯수", total4// 100)




