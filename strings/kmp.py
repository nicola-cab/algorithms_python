def build_dfa(pattern):
    """ build dfa """
    M = len(pattern)
    R = 128 
    dfa = [ [ 0 for x in range(M)] for x in range(R)]

    dfa[ord(pattern[0])][0] = 1

    X = 0
    for j in range(1, M):
        #copy other states
        for c in range(R):
            dfa[c][j] = dfa[c][X] 
        
        index = ord(pattern[j]) 
        #move from current state to next state
        dfa[index][j] = j+1
        #start to compute next state
        X = dfa[index][X]

    return dfa


def pattern_matching(str,pat):
    """ pattern matching using kmp"""
    i,j,N,M = 0,0,len(str), len(pat)
    dfa = build_dfa( pat )

    while i < N and j < M: 
        index = ord(str[i]) 
        if index < 0:
            break

        j = dfa[index][j]
        i += 1

    if j == M:  return i - M
    raise Exception("Pattern not found")

if __name__ == "__main__":
    try:
        i = pattern_matching( "mondo ciao eccoci", "eccoci")
        print("Pattern found, start index = ", i)
    except Exception as e:
        print(e)
