if __name__ == "__main__":
    from queue import queue
    
    print("Queue test")
    q = queue()
    
    #dequeue from empty queue.. exception waited
    print("is queue empty ? ", q.isEmpty())
    try:
        q.dequeue()
    except Exception as e:
        print(e)
    
    #test enqueuing in queue
    list_s = ["hello", "cruel", "world"]
    for s in list_s:
        q.enqueue(s)
    
    #test iteration
    print("Iteration over queue")
    for item in q:
        print("-> ",item)
    
     #checking last element in queue
    print("(FIFO) First Output Element -->", q.last())
    
    #test dequeueing 
    print("Dequeue operation")
    for i in range(0,q.size()):
        print(q.dequeue())
    
    print("is queue empty ? ", q.isEmpty())

    
        
    
