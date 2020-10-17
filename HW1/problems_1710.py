# 1
def solution(*args):
    return '-'.join(args[::-1])
# 2
factorial = lambda x: 1 if x == 0 else x * factorial(x - 1)
list(map(factorial, filter(lambda x: x % 3 == 0, range(51))))

# 3
def solution_3(n):
    res = [n[x] for x in range(len(n)) if x % 2 != 0]
    # res1 = [x for y, x in enumerate(n) if y % 2 != 0]
    return res

# 4

 
def sum_digits(num):
    sum_dig = 0
    for i in str(num):
        sum_dig += int(i)
    return sum_dig

def solution_4(num_list):
    result = [x for x in num_list if sum_digits(x) <= 10]
    return result

