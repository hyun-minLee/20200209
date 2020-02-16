

try:
    w=float(input("직사각형의 가로의길이를 입력하시오"))
    h=float(input("직사각형의 세로의길이를 입력하시오"))
    area=(w*h)
    perimeter= 2*(w+h)
    print("사각형의 넓이", area)
    print("사각형의 둘레", perimeter)

except ValueError:
    print("실수값을 입력하시오")
