from base.utils import less_comparator, greater_comparator 
import random

def test_order(a, cmp):
    for i in range(1, len(a)):
        if not cmp(a[i-1],a[i]):
            return False
    return True

def is_ascending_order(a):
    """ test if vector is sorted in ascending order"""
    return test_order(a, less_comparator)

def is_descending_order(a):
    """ test if vector is sorted in descending order"""
    return test_order(a, greater_comparator)

def generate(size, seed):
    """ generate list of numbers """
    return [int(seed*random.random()) for i in range(size)]
