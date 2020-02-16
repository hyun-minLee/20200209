# py04_02_ifelse

# 하나의 점수를 입력 받고, 입력 받은 점수에 해당하는 학점을 출력하는 프로그램을 작성하시오.
# 입력 받는 정수는 0~100까지이고    
# 90점 이상이면 A,    
# 80점 이상이면 B,    
# 70점 이상이면 C,   
# 60점 이상이면 D,    
# 나머지는 F

grade=int(input("성적을 입력하시오"))
if 90<=grade <=100:
    print("A")
elif 80<=grade<90:  #elif = if else
    print("B")
elif 70<=grade<80:
    print("C")
elif 60<=grade<70:
    print("D")
else:
    print("F")