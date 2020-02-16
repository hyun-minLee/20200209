x =3
y =4

r= ((x==3) and (y==3))
print("(x==3) and (y==3):",r )

r=((x==3) and (y!=3))
print("(x==3) and (y!=3):", r)

r=((x==3) or (y==3))
print("(x==3) or (y==3):", r)

r=((x==3)or (y==4))
print("(x==3)or (y==4):", r)

r =((x!=3)or (y==4))
print("(x!=3 || (y==4):", r)

r=((x!=3)or (y!=4))
print("(x!=3) || (y!=4):", r)

x =3
y =4    
print("#############################")

print((x==y) and (x !=y )) #false
print((x >y )or (x< y)) #true
print((x >=y) or (x<=y)) #true
print((x==y) and ( x!=y) or (x<y)) #true