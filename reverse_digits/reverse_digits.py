def digitize(n):
    digits = list(str(n))
    digits.reverse()
    for i in range(0, len(digits)):
        digits[i] = int(digits[i])
    
    return digits