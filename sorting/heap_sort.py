#
#   Implementation of heap sort. 
#   Algorithm not good in practise even if it requires N lg N time to sort in all cases.
#   - This is algorithm is slow in practise because is less cache friendly than quick-sort
#

from base.pq import pq

def heap_sort( list , cmp ):
    N = len(list)
    pq_ = pq(cmp) #comparator passed will make a min or max heap

    for i in range(0,N):
        pq_.insert(list[i])
    
    for i in range(0, N):
        list[i] = pq_.delElem()
    
