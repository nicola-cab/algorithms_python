def shell_sort(a, cmp):
    """
        shell sort performs a h sort. where h is parameter defined by the implementation.
        The rule is that during the i-th iteration everything between a[i] and a[h] is swapped
        accordigly with comparator provided.
        Notice that a[i] is the pivot in and the index is moved from i to h.

        worst case N^3/2
        avg .... 
        best case N lg3 N
    """

    N = len(a)
    h = 1
    #find 1/3 of this array (note this parameter depends by the implementation. this is empiric 
    while h < N/3:  
        h = 3*h+1  
    
    #till I do not process all the elements
    while h>= 1:
        #run the check for h to N
        for i in range(h, N):
            j = i
            #process h-ranges [i, h]
            while j >= h:
                if cmp(a[j], a[j-h]):
                    a[j], a[j-h] = a[j-h], a[j] 
                j=j-h
        h=h/3

