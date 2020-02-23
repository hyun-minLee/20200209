
x= []
x=input("입력하시오")
print(x[0], x[1], x[2], x[3])
#y=len(x)
#print(y)
y=0
sum=0
while y<len(x):
    sum=int(x[y])+ sum
    y=y+1
print("자리수의합은", sum)    
    
    
    
a=int(x[0])
b=int(x[1])
c=int(x[2])
d=int(x[3])
sum=a+b+c+d
print("자리수의합은", sum)
