class AgeInvalidException(Exception):
    pass

def checkAge(age):
    if age<18:
        raise AgeInvalidException("age is below 18")
    else:
        print(f"{age} is eligible")
        
        
try:
    checkAge(12)
except AgeInvalidException as e:
    print("error:",e)
finally:
    print("code executed")