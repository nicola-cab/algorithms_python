def compute_table( pattern ):
    """ compute a table to decide how much skip doing pattern matching """
    M = len( pattern )
    R = 128
    right = [-1 for x in range(R)]
    for j in range(M):
        right[ ord(pattern[j]) ] = j

def pattern_matching(str, pattern):
    pass
