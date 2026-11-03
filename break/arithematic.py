while True:
 num1=int(input("enter the number"))
 num2=int(input("enter the number"))

 print("1.addition")
 print("2.substraction")
 print("3.multiplication")
 print("4.exit")

 ch=int(input("enter the choice"))

 match ch:
    case 1:
        print("addition is",num1+num2)
    case 2:
        print("substraction is",num1-num2)
    case 3:
        print("multiplication is",num1*num2)    
    case 4:
          print("exit")
          break