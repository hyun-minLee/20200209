# 리스트의 CRUD3S
# C: create.
# R: read
# U: update
# D: delete
# S: search
# S: sort
# S: shuffle


############################
# 리스트 선언

# 공백 리스트 생성
# 문자 H, e, l, l, o를 요소로 가지는 리스트
# 문자열 Hello를 요소로 가지는 리스트
# 0, 1, 2, 3, 4를 요소가 가지는 리스트 생성
# 공백 리스트 생성
# 문자열을 리스트로 변환. 문자 H, e, l, l, o를 요소로 가지는 리스트 생성
# 0, 1, 2, 3, 4를 요소가 가지는 리스트 생성
############################
############################
# 리스트 요소 출력
############################

############################
# 리스트 출력
############################

############################
# 리스트 슬라이싱
############################

############################
# 리스트 요소 대입
############################

############################
# 리스트 열거
############################

############################
# 복잡한 리스트
# 1차원 리스트
# 2차원 리스트
# 3차원 리스트
############################


############################
# 리스트에 담을 수 있는 것은?
# 리스트 선언
# 리스트 대입
# 리스트 출력
# 리스트 열거
# 리스트에 저장된 함수 실행하기
############################

############################
# 문자열 vs 리스트
############################

array= [273, 32, 103, "문자열", True, False]
print(array)

array = [1, 1.1, "문자", True, [0,1], {"a":1, "1":"ba"}, None]
print(array)

list1 = ["H", "e", "l", "l", "o"]
print(list1, type(list1))

list2 = ["Hello"]
print(list2, type(list2))

list3 =[0,1,2,3,4,]
print(list3, type(list3))

list4= list(range(0,5,1))
print(list4, type(list4))

list5= list("Hello")
print(list5, type(list5))


array = [1, 1.1, "문자", True, [0,1], {"a":1, "1":"ba"}, None]

print(type(array[0]), array[0])
print(type(array[4]), array[4])
print(type(array[5]), array[5])
print(type(array[6]), array[6])

print(array)

print(array[1:3])
print(array[-1])
print(array[-4])

array[0]="변경"
print(array)

#list에 추가(리스트 마지막에 넣는다)  .append()메서드 사용
#list에 삽입(리스트 중간에 넣는다=특정위치를 지정하고) .insert() 메서드 사용
array.append("추가")  #list에 맨마지막방에 "추가"라는 문자열이 삽입된다.
print(array)

array.insert(0, "삽입")   #list에서 0번방에 "삽입"이라는 문자열이 삽입된다.
print(array)

#list요소 삭제: 메서드 이용하는 방식 .pop()   <----추천  값을빼놓고 그것을 저장하고있는 메모리가있다.(꺼내서 어딘가에 재사용가능)
#list요소 삭제: 연산자 이용하는 방식 del

array.pop(0)  #list에서 0번째의 요소의값을 삭제한다.  
print(array)

del array[0]  #list에서 0번쨰의 요소의 값을 삭제한다.
print(array)

for i in range(0, len(array), 1):
    print(array[i], end=" /")

