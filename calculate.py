import user_interface as ui

one = 0
two = 0
sign = ''

def init (one_num,two_num):
    global one
    one = one_num
    global two
    two = two_num

def distribution(sign):
    if (sign == '+'): return sum()
    elif(sign == '-'): return sub()
    elif(sign == '*'): return mult()
    elif(sign == '/'): return div()

def sum():
    return one + two

def mult():
    return one * two

def sub():
    return one - two

def div():
    return one / two



