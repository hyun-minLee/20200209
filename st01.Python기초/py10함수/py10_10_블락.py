def add(a, b):  # 함수를 만들때는 def
    sum = 0
    for i in range(x, y+1, 1):
        sum = sum+i    
    return sum


#a = int(input("정수를 입력하시오"))
#b = int(input("정수를 입력하시오"))


x = 3
y = 7
result = add(x, y)
print(result)

# 변수의 종류
# 전역변수 if,for,함수 안에 있지않은 변수가 전역변수이다 ex) x,y 전역변수는 함수에서 접근이 가능하다.
# 지역변수 sum, i
# 매개변수 a,b
