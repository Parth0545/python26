class PaymentError(Exception):
    pass

class CardDeclinedError(PaymentError):
    pass

class PaymentTimeoutError(PaymentError):
    pass


def Process_Payment():
    raise CardDeclinedError("the card has been declined")


try:
    Process_Payment()
except PaymentError as e:
    print("Payment cancel",e)
finally:
    print("program executed successfully")
    

    
    
    