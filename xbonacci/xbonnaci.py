def Xbonacci(signature, n):
    bracket = len(signature)
    for x in range(0, n - bracket):
        newValue = 0
        for i in range(1, bracket + 1):
            newValue += signature[-i]
        signature.append(newValue)
    return signature[:n]
