

def sum(a,b):
    return a + b

def max1(a,b):
    '''in: a:int, b:int, return: größere vom zwei Zahlen  '''
    return a if a > b else b

def max2(li:list[float]):
    if not li:
        raise ValueError("List must not be empty!")
    max_value=li[0]
    for i in range(1, len(li)):
        if li[i] > max_value:
            max_value = li[i]
    return max_value

def div(a,b):
    if b == 0:
        raise ZeroDivisionError('nicht durch 0 teilen!')
    return a / b



