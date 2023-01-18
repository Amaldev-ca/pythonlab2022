#n=int(input("enter the number"))
#fact=1
#for i in range(1,n+1):
 #   fact=fact*i
#print("factorial is:",fact)
def calc_factorial(x):
    if x==1:
        return 1
    else:
        return(x*calc_factorial(x-1))
num=int(input("enter a number"))
print("the factorial of","is",calc_factorial(num))