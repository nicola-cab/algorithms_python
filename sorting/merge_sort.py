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
        self.__a = a
        self.__cmp = cmp
        self.__a = self.__sort(self.__a)

    def get(self):
        """ get the collection sorted using comparator passed to this class"""
        return self.__a
        
    def __sort(self, list):
        """ implement recursion and splitting in halves """
        
        N = len(list)
        if N <= 1:
            return list

        #
        #here to really optimize the algorithm. run some faster sort algorithm for small N and return.
        #

        left = []
        right = []
        m = N//2

        for x in list[:m]:
            left.append(x)

        for x in list[m:]:
            right.append(x)

        left  = self.__sort(left)
        right = self.__sort(right)
        return self.__merge(left,right)


    def __merge( self, left, right):
        """
        merge function:
            - meld 2 list: left and right in only one.
        """
        result = []
 
        #merge left and right
        while left and right:
            if self.__cmp(left[0],right[0]):
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
