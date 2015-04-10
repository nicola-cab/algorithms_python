#
#  - couting sort algorithm. This sort operates in linear time N+k time and space.
#  - where k --> number of keys
#  - where N --> size of collection to sort
#
#   counting sort is useful in radix sort as subrouting to sort all the buckets
#

def counting_sort(list, k):
    """ 
        basic idea is:
            - build histogram for keys
            - copy back histogram in to sorted array and return it
    """
    
    n = len(list)
    count = [0] * (k + 1)
    
    #make histogram
    for i in range(n):
        count[list[i]] += 1
    
    #serialize histogram in result vector. Note this operation take linear time
    p = 0
    for i in range(k):
        for j in range(count[i]):
            list[p] = i
            p += 1
