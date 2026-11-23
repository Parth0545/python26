def average():  
    num=int(input("enter the how many number"))
    
    sum=0
    for i in range(num):
        num=float(input("enter the number"))
        sum=sum+num
        
    avg=sum/num
    return avg

result=average()
print("Average is",result)
