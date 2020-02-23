
# 1부터 10까지의 합계를 구하고
# 그 합계를 sum에 저장하고 sum 값을 한번만 출력한다.

# 1부터 100까지의 합계를 구하고
# 그 합계를 sum2 에 저장하고 sum2 값을 한번만 출력한다.

# 100부터 sum2까지의 합계를 구하고
# 그 합계를 sum3 에 저장하고 sum3 값을 한번만 출력한다.


def add(a, b):                #함수를 만들때는 def
    sum=0
    for a in range(a, b+1, 1):
        sum = sum+a
        a = a+1
    return sum


a = int(input("정수를 입력하시오"))
b = int(input("정수를 입력하시오"))

if a > b:
    temp = a
    a = b
    b = temp

result = add(a, b)
print(result)
