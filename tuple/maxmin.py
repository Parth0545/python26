t1=(10,30,50,70,90)
t2=(20,40,60,80,100)



maximum=t1[0]
minimum=t1[0]



for i in t1+t2:
    if i > maximum:
        maximum=i
    if i < minimum:
        minimum=i
        
    print(maximum)
    print(minimum)
