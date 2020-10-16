def solution(a, b):
    result = a[:] # otherwise they will have the same id
    for x in b:
        if x not in a:
            result.append(x)
    return sorted(result)
    
