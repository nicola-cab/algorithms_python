#
#    merge sort implementation. 
#    This is a perfect sorting algorithm since meets the lower bound for sorting.
#        it sorts a sequence of numbers in n lg n (best,avg,worst).
#        Basic idea:
#            - divide collection of items passed in 2 halves 
#                (in this implementation I am using extra allocation for these lists) I 
#            - recursive sort each half
#            - merge two halves
#
#

def merge_sort(list, cmp):
    """ implement recursion and splitting in halves """
        
    N = len(list)
    if N <= 1:
        return list

    # from selection_sort import selection_sort
    #optimization here: use a simple and faster algorithm for a small list size.
    #if len(list) < 20:
    #    selection_sort(list, cmp)
    #    return list

    left = []
    right = []
    m = N//2

    for x in list[:m]:
        left.append(x)

    for x in list[m:]:
        right.append(x)

    left  = merge_sort(left, cmp)
    right = merge_sort(right, cmp)
    return merge(left,right, cmp)


def merge( left, right, cmp):
    """
    merge function:
        - meld 2 list: left and right in only one.
    """
    result = []
 
    #merge left and right
    while left and right:
        if cmp(left[0],right[0]):
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]
        
    #add what it's left in left list
    if left:
        result += left

    #add what it's left in right list
    if right:
        result += right

    return result;