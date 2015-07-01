def loop_size(node):
    tortNode = node
    hareNode = node.next.next
    while True:
        tortNode = tortNode.next
        hareNode = hareNode.next.next
        if (hareNode.next == tortNode) or (hareNode == tortNode):
            break

    lapNode = tortNode.next
    searchNode = lapNode.next
    loopSize = 1
    while True:
        if searchNode == lapNode:
            break
        searchNode = searchNode.next
        loopSize += 1
    return loopSize