
i=0
sum=0
while i<101:
    i=i+1
    if  i % 3 == 0:
        sum= sum+i
    else:
        print("i의값은 %d" %i)
print("sum의값은", sum) 