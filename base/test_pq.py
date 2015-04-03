def test_priority_queue(testName,comparator):
    from pq import pq
    print("Testing ", testName, " priority queue")
    heap_pq = pq(comparator)

    for i in range(0,10):
        heap_pq.insert(i)
    
    #pop from priority queue 
    for i in range(0, heap_pq.size()):
        for key in heap_pq:
            print("\n Cycle number", i, " - Element in pq -->", key)

        print( "\n Cycle number", i, " --> Getting  ", testName, " element in current priority queue ->",heap_pq.delElem())

if __name__ == "__main__":
    from utils import less_comparator
    from utils import greater_comparator
    test_priority_queue( "Min", less_comparator )
    print("-------------------------------------------")
    test_priority_queue( "Max", greater_comparator)
