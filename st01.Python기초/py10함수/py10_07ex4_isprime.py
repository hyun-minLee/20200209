

def isprime(n):
    for x in range(2, n, 1):
        if n%x ==0:                  
            return False
    return True
        

n=int(input("정수의값을 입력하시오"))
result= isprime(n)           
bool(result)
print("정수의값을 입력하시오%s" %result)




