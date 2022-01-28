def is_armstrong_number(number):
    s = str(number)
    l = len(s)
    total = sum([int(i)**l for i in s])
    return number == total
    
# vim:ts=4:sw=4:expandtab
