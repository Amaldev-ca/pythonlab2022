class time:
    def __init__(self):
        self.__h=float(input("enter the time in hour:"))
        self.__m=float(input("enter the time in minuts:"))
        self.__s=float(input("enter the time in seconds:"))
    def __add__(self,tobj2):
        hours=self.__h+tobj2.__h
        print("sum of hours",hours)
        minuts=self.__m+tobj2.__m
        print("sum of minuts",minuts)
        seconds=self.__s+tobj2.__s
        print("sum of seconds",seconds)
        if hours>=24:
            hours=hours%24
        if minuts>=60:
            hours=hours+minuts//60
            minuts=minuts%60
        if seconds>=60:
            minuts=minuts+seconds//60
            seconds=seconds%60
        return hours,minuts,seconds
print("enter the time of the first object:")
tobj1=time()
print("enter the time of the second object:")
tobj2=time()
print("sum of two time is:(hour,minuts,seconds)",tobj1 + tobj2)



        
        
    
        