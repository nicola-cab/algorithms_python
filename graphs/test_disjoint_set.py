from disjoint_set import disjoint_set
if __name__ == "__main__":
    l = [0,1,2,3,4,5]
    s = disjoint_set(l)
    s.union(5,1)
    s.union(1,2)
    s.union(1,3)
    s.union(4,0)
    
    print("Are component 5 and 4 connected = ", s.connect(5,4))
    print("Are component 5 and 3 connected = ", s.connect(5,3))
    print("Connecting 5 and 4")
    s.union(5,4)
    print("Are component 5 and 4 connected = ", s.connect(5,4))
    
    
    
    