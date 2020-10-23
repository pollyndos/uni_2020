def solution(n,k):
    # n - number of people, k - step
    arr = [i for i in range(1, n + 1)]
    delete_index = (k - 1) % len(arr) # k - 1 bc we need an index, % if k > n
    while len(arr) != 1:
        arr.pop(delete_index)
        delete_index = (delete_index + k - 1) % len(arr) # % bc we need to get correct index, when get (delete_index + k - 1) > len
    return arr[0]
