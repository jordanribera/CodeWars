def tribonacci(signature, n):
    seq = signature
    if sum(signature) > 100 or n == 0:
        return []
    if n < len(signature):
        return signature[-n:]
    for i in range(0, n - len(signature)):
        seq.append(seq[-1] + seq[-2] + seq[-3])
    return seq[-n:]
