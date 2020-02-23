# 중첩 for문
for x in range(2, 20, 1):
    for y in range(1, 10, 1):
        if y == 9:
            print("%2d x %d= %3d" % (x, y, x*y), end=", ")
        else:
            print("%2d x %d= %3d" % (x, y, x*y), end=". ")
print()
