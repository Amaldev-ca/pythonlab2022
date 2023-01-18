import calfunction
a=int(input("enter the first element"))
b=int(input("enter the second element"))
choice=int(input("enter the choice\n1.Addition\n2.substraction\n3.multiplication\n4division:"))
if choice==1:
     print(a,"+",b,"=",calfunction.sum(a,b))
elif choice==2:
     print(a,"-",b,"=",calfunction.sub(a,b))
elif choice==3:
     print(a,"*",b,"=",calfunction.mul(a,b))
elif choice==2:
     print(a,"/",b,"=",calfunction.div(a,b))
else:
     print("invalid choice")