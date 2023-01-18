class Rectangle:
    def __init__(self):
        self.__length=int(input("enter the length of the reactangle:"))
        self.__breadth=int(input("enter the breadth of the reactangle:"))
    def __lt__(self,R2):
        area1=self.__length*self.__breadth
        area2=R2.__length*R2.__breadth
        print("Area of Rectangle 1 is:",area1)
        print("Area of Rectangle 2 is:",area2)
        return area1<area2
print("enter the length and breadth of first reactangle:")
R1=Rectangle()
print("enter the length and breadth of second reactangle:")
R2=Rectangle()
if R1<R2:
    print("Rectangle 1 is less than Reactangle 2")
else:
    print("Rectangle 1 is greater than  Reactangle 2...!")
    