class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def get_perimeter(self):
        return 2 * (self.length + self.breadth)
    def get_area(self):
        return self.length * self.breadth
    def compare(self,a):
         try:
             if r.get_area()==a.get_area():
                 print("Both area are equal")
             elif r.get_area()>a.get_area():
                  print("largest area is:",r.get_area())
             else:
                  print("largest area is:",a.get_area())
         except:
                print("No Exception")
l1=int(input("enter the length of first rectangle:"))
b1=int(input("enter the breadth of first rectangle:"))
l2=int(input("enter the length of second rectangle:"))
b2=int(input("enter the length of second rectangle:"))
r=Rectangle(l1,b1)
print("Area of rectangle:",(r.get_area()))
print("Perimeter of rectangle:",(r.get_perimeter()))
a=Rectangle(l2,b2)
print("Area of rectangle:",(a.get_area()))
print("Perimeter of rectangle:",(a.get_perimeter()))
r.compare(a)