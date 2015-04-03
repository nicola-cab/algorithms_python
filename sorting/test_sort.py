if __name__ == "__main__":
    import sys
    from os import path
    sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

    from selection_sort import selection_sort
    from base.utils import less_comparator, greater_comparator
    from utils import generate, is_ascending_order, is_descending_order

    print("Test sorting algorithms")
    a = generate(10,10)
    print(a)

    a = selection_sort(a, less_comparator)
    print(a) 
