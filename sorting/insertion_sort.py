def insertion_sort(a, cmp):
    """ 
        Insertion sort algorithm performs N^2 comparisons and exchanges in the worst case (array sorted in desceding order).
        In the best case the algorithm performs N-1 comparisons and 0 exchanges.

        The base idea is slide throughout the array and keep this invarinat:
            - Elements on left to current index are already sorted in ascending way
            - Elements on the right must be checked
    """
    for i in range(0,len(a)):
        j = i
        while j>0 and cmp(a[j],a[j-1]):
            a[j],a[j-1] = a[j-1],a[j]
            j = j - 1
        
