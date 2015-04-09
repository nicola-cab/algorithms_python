#
#   functional_quick_sort: 
#   (note this quick sort is inspired from a functional version of it... for this reason I called it in this way)
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
            # from selection_sort import selection_sort
            # from base.utils import less_comparator 
            #optimization here: use a simple and faster algorithm for a small list size.
            #if len(list) < 20:
            #    selection_sort(list, less_comparator)
            #    return list
            
            # run normal quick_sort        
            less,equal,greater = partition(list)
            less    = functional_quick_sort(less)
            greater = functional_quick_sort(greater)
            return less + equal + greater

            
#
# classical hoare quick sort.
#   - in this algorithm a classical quick sort is implemented using Hoare partition function.
#       - idea:
#           divide and conquer the list passed.
#           - using two indexes i and j to scroll the list from left to right and from right to left. 
#           - scroll using i till all the elements are less or equal than pivot
#           - scroll using j till all the elements are greater than pivot
#           - swap i and j content if i<=j

def quick_sort(list):

    # from selection_sort import selection_sort
    # from base.utils import less_comparator 
    #optimization here: use a simple and faster algorithm for a small list size.
    #if len(list) < 20:
    #    selection_sort(list, less_comparator)
    #    return

    import random
    random.shuffle(list)
    __quick_sort(list,0,len(list)-1)

def __quick_sort(list,s,e):
    if e<=s: 
        return
    
    p,q = hoare_partition(list, s, e)
    __quick_sort(list, s, p-1)
    __quick_sort(list, q+1, e)    
    
def hoare_partition(list, s, e):
    
    begin = s 
    end = e
    v = list[begin]
    i = begin

    #3-way quick sort.
    while i <= end:

        #all left to v
        if list[i] < v:
            list[begin], list[i] = list[i], list[begin]
            i += 1
            begin += 1
        
        #all right to v
        elif list[i] > v:
            list[end], list[i] = list[i], list[end]
            end -= 1

        #all equal to pivot
        else:
            i += 1

    return begin,end
