import user_interface as ui

def convert():
    source = ui.data_input()
    expression = source.split()
    if ('i' in source or 'j' in source):
        return convert_complex(expression)
    else:
        return convert_rational(expression)

def convert_complex(expr):
    expr[1] = expr[1] + expr[2]
    expr[5] = expr[5] + expr[6]
    expr.pop(2)
    expr.pop(5)
    expr = list(map(lambda el: el.replace('i',''),expr))
    expr[0] = complex(int(expr[0]),int(expr[1]))
    expr[3] = complex(int(expr[3]), int(expr[4]))
    expr.pop(1)
    expr.pop(3)
    return expr

def convert_rational(expr):
    expr[0] = int(expr[0])
    expr[2] = int(expr[2])
    return expr



