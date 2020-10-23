def solution(arr):
    res = []
    while len(arr) > 0:
        # 1 - we add the whole first list, remove it
        res.extend(arr.pop(0)) #  extend() iterates over its argument and add the elements, while append() just add the argument
        # if only one element in one list was left, and now was added, we stop (when n is odd)
        if len(arr) == 0:
            break        
        for i in arr:
            # 2 - we add all last elements of each list, remove these elements
            res.append(i.pop(-1))
        # 3 - we add the whole reversed last list, remove it
        res.extend(arr.pop(-1)[::-1])
        for i in arr[::-1]:
            # 4 - we add all first elements of each remaining list in reversed order, remove these elemnts
            res.append(i.pop(0))
    return res

