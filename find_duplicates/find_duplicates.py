def duplicates(array):
    previously_found = []
    output = []
    for element in array:
        if element not in previously_found:
            previously_found.append(element)
        else:
            if element not in output:
                output.append(element)
    return output
