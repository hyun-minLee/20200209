# py02_09ex1_Salary

# 변수 선언 : salary , deposit 정수 변수 선언

# 정수를 입력받고 salary 변수 에 저장하시오.

# 10년치 월급의 총합을 구하고 그 값을 deposit 에 저장.

# 10년 동안의 저축액: ?????  원 형태로 출력하시오.

salary=0
deposit=0
i=1
while i != 10 :
    salary=input("급여를 입력하세요")
    salary=int(salary)
    deposit=int(salary+deposit)
    i=i+1
    
print("10년 deposit", deposit)