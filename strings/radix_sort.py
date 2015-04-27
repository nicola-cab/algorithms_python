def lsd( a, m, n):
    """
        Radix sort implementation.
        m = max number of symbols -> eg 10 
        n = max number of digits -> eg 5  

        complexity:
        worst case: O(wn)
    """
    for x in range (n):
        bins = [ [] for i in range(m) ]
        for item in a:
            bins[(item//(m**x))%m].append(item)
        a = []
        for bin in bins:
            a.extend(bin)
    return a

def lsd_str(a):
    """
        Radix sort for strings.
    """
    #find longest string in array
    max_len = 0
    for s in a:
        if len(s) > max_len:
            max_len = len(s)
    #calculate code for a and z
    ss = ord('a')
    es = ord('z')
    n = es - ss #define number of symbols
    for pos in range( max_len ):
        bins = [ [] for i in range(n) ]
        for s in a:
            index = 0
            if pos < len(s):
                index = ord(s[pos]) - ss
            bins[index].append(s)
        a = []
        for bin in bins:
            a.extend(bin)
    return a

if __name__ == "__main__":
    import random
    a  = [random.randint(0, 10) for i in range(5)]
    print("Array generated (int):")
    print(a)
    a = lsd(a, 10, 2)
    print("After radix sort")
    print(a)

    a = [ "ciao" , "sono" ,"proprio" , "io" ]
    print("Before radix sort (strings): ",a)
    a = lsd_str(a)
    print("After radix sort (strings):", a)
