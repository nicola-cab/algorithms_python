def compute_table( pattern ):
    """ compute a table to decide how much skip doing pattern matching """
    M = len( pattern )
    R = 128
    right = [-1 for x in range(R)]
    for j in range(M):
        right[ ord(pattern[j]) ] = j

    return right

def pattern_matching(str, pattern):
    N = len(str)
    M = len(pattern)
    table = compute_table(pattern)
    skip = 0
    for i in (0, N-M, skip):
        skip = 0
        for j in range(M-1, -1, -1):
            if pattern[i] != str[i+j]:
                pass

if __name__ == "__main__":
    table = compute_table("ciao")
    print(table)
