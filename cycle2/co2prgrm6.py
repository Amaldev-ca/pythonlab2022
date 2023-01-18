str=input("enter a word")
c=0
for i in str:
    if i==" ":
        continue
    else:
        c+=1
print(c,"characters in "+str)