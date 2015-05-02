def pattern_matching(str, pattern):
    """
    Brute force pattern matching.
    """

    N = len(str)
    M = len(pattern)

    if N<M:
        raise Exception("assumption is N >= M")

    for i in range(N-M+1):
        j = 0
        while j < M:
            if str[i + j] != pattern[j]:
                break
            j += 1

        if j == M:
            return i

    raise Exception("Pattern not found")

if __name__ == "__main__":
    try:
        i = pattern_matching( "mondo ciao", "ciao")
        print("pattern found at starting = ", i)
    except Exception as e:
        print(e)
