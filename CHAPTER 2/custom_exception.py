
def check_age(age):
    if age<0:
        raise ValueError("age cant be negative")
    else:
        print("age is positive " )

    
try:
    check_age(-3)
except ValueError as e:
    print("error",e)
finally:
    print("code executed")