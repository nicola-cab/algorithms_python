#
#   functional_quick_sort:
#       - split recursively list in 3 lists:
#           - list less than pivot
#           - list equal to pivot
#           - list greater than pivot
#       - merge list back and return
#       - not optimization has made... 
#       
#       note: this quick sort is not as fast as a index based one. due list allocations
#
def partition(list):
    pivot = list[0]
    less    = [x for x in list if x < pivot] 
    equal   = [x for x in list if x == pivot]
    greater = [x for x in list if x > pivot]
    return less,equal,greater
    
    
def functional_quick_sort(list):
        import random
        random.shuffle(list)

        if len(list) < 1:
            return list
        
        else:
            #optimization here: use a simple and faster algoirithm for a small list size.

            less,equal,greater = partition(list)
            less    = functional_quick_sort(less)
            greater = functional_quick_sort(greater)
            return less + equal + greater
