'''fn1=open("file.txt",'r')
lines=fn1.readlines()
l1=[line.strip() for line in lines]
print(l1)'''
#print([line.strip()for line in open('file.txt','r')])

'''fn=open("file.txt",'r')
s=fn2=.readline()
l=s.split()
print(l)
fn.close'''

fn1=open("file.txt",'r')
s=fn1.readlines()
for x in range(0,len(s)):
    print(s[x])
fn1.close