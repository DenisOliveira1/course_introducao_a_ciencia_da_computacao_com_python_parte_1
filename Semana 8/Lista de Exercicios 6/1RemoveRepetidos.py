def remove_repetidos(n):
    for i in n:
        if n.count(i) > 1:
            while n.count(i) != 1:
                del n[n.index(i)]
    n.sort()
    return n

            
        
    
