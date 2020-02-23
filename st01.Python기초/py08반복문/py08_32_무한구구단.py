while True:
    try :
        x = int(input("숫자를 입력하시오"))
        y = int(input("숫자를 입력하시오"))
    except ValueError:
        print("정수를 입력하시오")
        break
    
    if x <0 or y <0:
        print("양수값을 입력하시오.")
        break

    if x > y:   
        temp = x
        x = y
        y = temp
                 
    for x in range(x, y+1, 1):
    
        for y in range(1, 10, 1):
            if y == 9:
                print("%2d x %d= %3d" % (x, y, x*y), end=", ")
            else:
                print("%2d x %d= %3d" % (x, y, x*y), end=". ")
        print()
