#
#  Statistic order implementation of quick_select 
#   to find the k-th element in to list of values.
#   This algorithm takes linear time. 
#

def quick_select(list, k):
    """ Quick select implementation. Return the k-th value for a collection of items"""
    
    from quick_sort import hoare_partition
    import random
    random.shuffle(list)
    
    s = 0
    e = len(list) -1
    
    while( e > s ):
        p = hoare_partition(list, s, e)
        if p < k:
            s = p + 1
        elif p > k:
            e = p - 1
        else:
            return list[k]
    
    return list[k]
    
if __name__ == "__main__":
    #fix import issues
    import sys
    from os import path
    sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
    
    #import array generator
    from utils import generate
    
    a = generate(10, 100)
    print(a)
    
    min_el = quick_select(a, 0) # find min
    median = quick_select(a, len(a)//2) #find the median
    max_el = quick_select(a, len(a)-1) #find max
    
    print("The min is = " , min_el)
    print("The median is = " , median)
    print("The max is = " , max_el)
    
    