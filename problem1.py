import re
n=int(raw_input(""))
lst=[]
for i in range(n):
    b=raw_input("")
    lst.append(b)

for i in range(n):
    if(re.search('[a-z0-9]+@[a-z]+[.]?com$', lst[i])):
        print(lst[i])
