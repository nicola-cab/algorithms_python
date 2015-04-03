if __name__ == "__main__":
    from stack import stack 
    
    print("Stack testing")
    s = stack() 
    
    #pop from empty stack.. exception waited
    print("is stack empty ? ",s.isEmpty())
    try:
        elem = s.pop();
    except Exception as e:
        print("Caught exception:",e)
    
    #test pushing elements
    for i in range(0,10):
        s.push(i)
    
    #look to peek and size of the stack
    print("Stack peek =",s.peek())
    print("Stack size =",s.size()) 
    
    #test iteration
    print("Reverse Iteration over stack")
    for item in s:
        print("-> ",item)
    
    #test popping elements
    for i in range(0,10):
        el = s.pop()
        print("Element popped = ", el )
    
    print("is stack empty ? ",s.isEmpty())

    