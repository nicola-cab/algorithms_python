if __name__ == "__main__":
    import sys
    from os import path
    sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

    from selection_sort import selection_sort
    from insertion_sort import insertion_sort
    from shell_short import shell_sort
    from merge_sort import merge_sort
    #from quick_sort import quick_sort

    from base.utils import less_comparator, greater_comparator
    from utils import generate, test_order, is_ascending_order, is_descending_order

    print("Test sorting algorithms")
    a = generate(5,5)
    a1 = a[:]
    a2 = a[:]
    a3 = a[:]
    a4 = a[:]
    print(a)

    print("Testing selection sort")
    selection_sort(a, less_comparator)
    print(a)
    print("Selection sort succeeded = " , test_order(a,less_comparator))

    print("Test insertion sort")
    insertion_sort(a1, less_comparator)
    print(a1)
    print("Insertion sort succeeded = ", test_order(a1, less_comparator))

    print("Test shell sort")
    shell_sort(a2, less_comparator)
    print(a2)
    print("shell sort succeeded = ", test_order(a2, less_comparator))

    print("test merge sort")
    object_ms = merge_sort(a3, less_comparator)
    print(object_ms.get())
    print("merge sort succeeded = ", test_order(object_ms.get(), less_comparator))

    #print("test quick sort")
    #quick_sort(a4, less_comparator)
    #print(a4)
    #print("quick sort succeeded = ", test_order(a3, less_comparator))







