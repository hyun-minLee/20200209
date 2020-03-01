temp3 = "74 874 9883 73 9 73646 774"


temp2 = []
temp2=temp3.split()
temp4 = ""

for x in range(0, len(temp2), 1):
    temp2[x] = int(temp2[x])

print(temp2)
temp2=sorted(temp2)
print(temp2)

sum=0
for x in range(0, len(temp2),1):
    sum=sum+temp2[x]

print(sum)

avg=sum/len(temp2)
print(avg)
max=max(temp2)
print(max)

