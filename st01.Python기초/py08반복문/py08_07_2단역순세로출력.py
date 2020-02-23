a = 2
print("역순 구구단 출력예제")
b = int(input("숫자를 입력하시오>>"))

for b in range(b, 0, -1):
    print("%d x %d = %d" %(a, b, a*b))
