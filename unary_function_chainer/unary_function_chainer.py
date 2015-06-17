def chained(functions):
    def doit(param):
        result = param
        for this_function in functions:
            result = this_function(result)
        return result
    return doit
