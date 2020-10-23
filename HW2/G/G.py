def solution(a, b):
    result = a[:] # copy of the fisrt list
    for x in b:
        if x not in a:
            # the sorting process
            for i in range(len(result)):
                # we need to find an element which is greater than x
                # and we insert x before this element
                if result[i] > x:
                    result = result[:i] + [x] + result[i:]
                    break
                # if there is no element that is greater than x,
                # or if it is equal to the last element
                # we add it in the end of the result list
                if x >= result[-1]:
                    result.append(x)
                    break                  
    return result
