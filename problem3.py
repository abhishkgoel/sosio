n=int(raw_input(""))
x=0
y=0
for i in range(1,n+1):
    x=(i*i)+x
    y=i+y
z=y**2
print z-x
