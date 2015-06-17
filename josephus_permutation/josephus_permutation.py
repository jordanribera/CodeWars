def josephus(items,k):
    print 'josephus_survivor(' + str(items) + ',' + str(k) + ')'

    if len(items) < 1:
        return []

    soldier_list = items
    kill_list = []
    kill_index = (k - 1) % len(soldier_list)
    
    while len(soldier_list) > 1:
        this_kill = soldier_list[kill_index]
        kill_list.append(this_kill)
        del soldier_list[kill_index]
        
        kill_index = (kill_index + (k - 1)) % len(soldier_list)
        
    kill_list.append(soldier_list[0])
        
    return kill_list
