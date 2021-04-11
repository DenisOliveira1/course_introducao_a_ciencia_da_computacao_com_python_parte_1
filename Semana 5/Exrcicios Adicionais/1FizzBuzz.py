def fizzbuzz(n):
    aux3 = False
    aux5 = False
    
    if n % 3 == 0:
        aux3 = True  
    if n % 5 == 0:
        aux5 = True

    if aux3 and aux5:
        return "FizzBuzz"
    elif aux3:
        return "Fizz"
    elif aux5:
        return "Buzz"
    else:
        return n
