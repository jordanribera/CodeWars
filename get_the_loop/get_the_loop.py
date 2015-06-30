def loop_size(node):
    pastNodes = []
    loopcount = 0
    searching = True
    while searching:
        if node.next in pastNodes:
            searching = False
        else:
            pastNodes.append(node.next)
            node = node.next
        loopcount += 1
        if loopcount > 10000:
            searching = False
    print loopcount
    print pastNodes
    return (len(pastNodes)) - (pastNodes.index(node.next))