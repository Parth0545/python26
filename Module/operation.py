import add as m
import sub as n
import mul as r
import div as s
class main:
    def add(self):
        
        a=int(input("enter the number"))
        b=int(input("enter the number"))
        print(m.add(a,b))
        
    def sub(self):
        
        a=int(input("enter the number"))
        b=int(input("enter the number"))
        print(n.sub(a,b))
        
        
    def mul(self):
        a=int(input("enter the number"))
        b=int(input("enter the number"))
        print(r.mul(a,b))
        
    def div(Self):
        a=int(input("enter the number"))
        b=int(input("enter the number"))
        print(s.div(a,b))
        
m1=main()
while True:
    print("\n")
    print(1,"addition")
    print(2,"substraction")
    print(3,"multiplication")
    print(4,"division")
    print(5,"exit")
    
    ch=int(input("\n enter the choice"))
    
    if ch==1:
        m1.add()
    elif ch==2:
        m1.sub()
    elif ch==3:
        m1.mul()
    elif ch==4:
        m1.div()
    elif ch==5:
        exit
        break
    else:
        print("invalid choice")
            