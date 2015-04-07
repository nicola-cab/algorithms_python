class merge_sort:

    def __init__(self,a,cmp):
        """
        merge sort implementation. Perfect sorting since meets the lower bound for a sort algorithm.
        it sorts a sequence of numbers in n lg n.
        Basic idea:
            - divide sequence in 2 halves
            - recursive sort each half
            - merge two halves
        """
        self.__cmp = cmp
        b =a[:]
        self.__sort(a, b, 0, len(a))
        
    def __sort(self, a, b, lo, hi):
        """ implement recursion and splitting in halves """
        if hi<=lo:
            return

        mid = lo + (hi-lo)//2
        self.__sort(a, b, lo, mid)
        self.__sort(a, b, mid+1, hi)
        self.__merge(a, b, lo, mid, hi)


    def __merge( self, a, b, lo, mid, hi):
        """
        merge function:
            - use tmp list
            - merge 2 halves
        """
        for i in range(0, hi):
            b[i] = a[i]

        i = lo
        j = mid + 1
        for k in range(0,hi):

            if i>mid:
                a[k] = b[j]
                j += 1

            elif j>hi:
                a[k] = b[i]
                i += 1

            elif self.__cmp(b[j], b[i]):
                a[k] = b[j]
                j += 1

            else:
                a[k] = b[i]
                i += 1

