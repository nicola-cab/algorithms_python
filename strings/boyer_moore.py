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
    i = 0
    while i <= N-M:
        skip = 0
        for j in range(M-1, -1, -1):
            if pattern[j] != str[i+j]:
                skip = max(1, j - table[ord(str[i+j])])
                break
        if skip == 0: 
            return i
        i += skip

    raise Exception("Pattern not found")

if __name__ == "__main__":
    try:
        i = pattern_matching("hi I am a pattern matching test", "test")
        print("Pattern found at index =", i)
    except Exception as e:
        print(e)
