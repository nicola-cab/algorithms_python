from heapq import heappush, heappop, heapify
from collections import defaultdict

def huffman_encoding( symbols):
    #prepare a priority queue
    heap = [[freq, [symbol, ""] ]for symbol, freq in symbols.items()]
    heapify( heap )
    while len(heap) > 1:
        #extract from pq other nodes
        left = heappop( heap )
        right = heappop( heap )

        #symbol freq for left subtree 
        for pair in left[1:]:
            pair[1] = '0' + pair[1]

        #symbol freq for right subtree    
        for pair in right[1:]:
            pair[1] = '1' + pair[1]
        
        #push on the heap the sum of freq + new leaves
        heappush( heap, [left[0] + right[0]] + left[1:]+right[1:])
    
    #sort symbols in place
    return sorted(heappop(heap)[1:], key=lambda p: ( len(p[-1]), p) )

if __name__ == "__main__":
    txt = "test for huffman encoding"
    symbols = defaultdict(int)
    for c in txt:
        symbols[c] += 1
    huffman = huffman_encoding(symbols)
    print "Symbol\t Weight\t Code"
    for p in huffman:
        print "%s\t %s\t %s" %(p[0],symbols[p[0]],p[1])


    
