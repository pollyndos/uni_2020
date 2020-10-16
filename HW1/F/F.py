def solution(n):
    num_2 = []
    cur_num = 1
    while cur_num <= n:
        num_2.append(cur_num)
        cur_num *= 2
    return num_2

