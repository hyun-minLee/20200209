

arr =[]

for x in range(0, 10, 1):
    y=input("값을 입력하시오")
    arr.append(y)
    arr[x]=int(arr[x])

print(type(arr), arr)
print("리스트 정렬전", arr)
arr.sort()
print("리스트 정렬후", arr)

print(max(arr))
print(min(arr))

