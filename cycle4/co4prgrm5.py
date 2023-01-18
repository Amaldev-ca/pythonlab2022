class publisher:
    def __init__(self,n):
        self.name=n
    def __display(self):
        print("name of publisher is");
class Book(publisher):
    def __init__(self,n,t,a):
        super().__init__(n)
        self.title=t
        self.author=a
    def display(self):
        print("title of the book is",self.title)
        print("author of the book is",self.author)
class python(Book):
    def __init__(self,n,t,a,p,pgs):
        super().__init__(n,t,a)
        self.price=p
        self.pages=pgs
    def display(self):
        print("publisher of the book is:",p1.name)
        print("title of the book is:",p1.title)
        print("author of the book is:",p1.author)
        print("price of the book is:",p1.price)
        print("pages of the book is:",p1.pages)
p1=python("python programming","introduction to python","jeeva jose",450,300)
p1.display()