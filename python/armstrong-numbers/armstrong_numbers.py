def is_armstrong(number):
    digits = (int(d) for d in str(number))
    count = len(str(number))
    total = sum(digit ** count for digit in digits)
    return number == total
    
# vim:ts=4:sw=4:expandtab
