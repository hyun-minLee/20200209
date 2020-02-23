#문자열은 수정할수 없다는 의미는 
#새롭게 메모리가 할당된다는 의미다.

str1="abc"
print(id(str1))
str2=str1   #str2에 "abc"라는 주소값의 복사가 일어난다.
print(id(str2))

str1="efg"  #신규 메모리가 할당된다.
print(id(str1))