def josephus_survivor(n,k):
    print 'josephus_survivor(' + str(n) + ',' + str(k) + ')'

    soldier_list = list(xrange(1, n + 1))
    
    kill_index = (k - 1) % len(soldier_list);
    
    while len(soldier_list) > 1:
        del soldier_list[kill_index]
        
        kill_index = (kill_index + (k - 1)) % len(soldier_list)
        
        
    return soldier_list[0]
