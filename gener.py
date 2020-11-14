def integers():
    i = 0
    while True:
        yield i
        i += 1

def squares():
    for x in integers():
        yield x * x

def take(n, gener):
    result = []
    try:
        for i in range(n):
            result.append(next(gener))  
    except StopIteration:
        pass
    return result
