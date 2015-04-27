def bubble_sort(a):
    """ bubble sort sorting """
    for i in range(len(a)):
        for k in range(len(a)-1, i, -1):
            if a[k] < a[k-1]:
                a[k], a[k-1] = a[k-1], a[k]
    return a

if __name__ == "__main__":
    import random
    a = [random.randint(0,100) for i in range(100)]
    a = bubble_sort(a)
    print(a)
