def selection_sort(a, cmp):
    """ 
        Insertion sort perform N*2 comparison and N exchanges. Running time is N*2.
        Algorithm idea is to scroll from left to right considering the current index we have:
        - Invariants:
            - entries on left of current index (included) are sorted in ascending order
            - no entry on the right of currenti index is smaller than entries on the left
    """
    for i in range(0,len(a)):
        min = i; 
        for j in range(i+1, len(a)):
            if not cmp(a[min], a[j]):
                min = j
        a[i],a[min] = a[min],a[i]    
