def is_valid_IP(string):
    if " " in string:
        return False
    groupings = string.split(".")
    if len(groupings) != 4:
        return False
    for group in groupings:
        if representsInt(group):
            if int(group) < 0 or int(group) > 255:
                return False
            if len(str(int(group))) != len(group):
                return False
        else:
            return False
    return True
    
def representsInt(string):
    try:
        int(string)
        return True
    except ValueError:
        return False