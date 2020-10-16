def solution(n, k):
    # n = num of people, k = num of apples
    each = k // n
    left = k % n 
    return each, left
