
student =[]

i=0
sum=0
while True:
    x=int(input("성적을 입력하시오"))
    if x !=-1:
        student.append(x)
        sum=sum+student[i]
        i=i+1
    else:
        break;

print("성적의합계는 %d" %sum)
print("성적의 평균은 %f" %(sum/len(student)))


