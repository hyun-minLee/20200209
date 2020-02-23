
a=2
print("2단출력")
for x in range(1, 10, 1):
    if x==9:
        print("%d의 값은=." %(x))
    else:
        print("%d의 값은=," %(x))
    print("%d X %d = %2d" %(a, x, a*x ))  
