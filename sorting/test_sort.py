if __name__ == "__main__":
    import sys
    from os import path
    sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

    from selection_sort import selection_sort
    from insertion_sort import insertion_sort
    from shell_short import shell_sort
    from merge_sort import merge_sort
    from quick_sort import functional_quick_sort
    from quick_sort import quick_sort
    

    from base.utils import less_comparator, greater_comparator, less_equal_comparator
    from utils import generate, test_order, is_ascending_order, is_descending_order

    print("Test sorting algorithms")
    a = generate(10,10) #list of 10 elements with elements in range [0,10)
    a1 = a[:]
    a2 = a[:]
    a3 = a[:]
    a4 = a[:]
    a5 = a[:]
    print(a)

    print("Testing selection sort")
    selection_sort(a, less_comparator)
    print(a)
    print("Selection sort succeeded = " ,is_ascending_order(a))

    print("Test insertion sort")
    insertion_sort(a1, less_comparator)
    print(a1)
    print("Insertion sort succeeded = ", is_ascending_order(a1))

    print("Test shell sort")
    shell_sort(a2, greater_comparator)
    print(a2)
    print("shell sort succeeded = ", is_descending_order(a2))

    print("test merge sort")
    a3 = merge_sort(a3, less_comparator)
    print(a3)
    print("merge sort succeeded = ", is_ascending_order(a3))

    print("test functional quick sort")
    a4 = functional_quick_sort(a4)
    print(a4)
    print("functional quick sort succeeded = ", is_ascending_order(a4))
    
    print("test hoare quick sort")
    quick_sort(a5)
    print(a5)
    print("quick sort succeeded = ", is_ascending_order(a5))








