def less_equal_comparator(a,b):
    return a<=b

def greater_comparator(a,b):
    return not(less_equal_comparator(a,b))

def less_comparator(a,b):
    return a<b

def greater_equal_comparator(a,b):
    return not(less_comparator(a,b))

def equal_comparator(a,b):
    return a == b

def not_equal_comparator(a,b):
    return not equal_comparator(a,b)
