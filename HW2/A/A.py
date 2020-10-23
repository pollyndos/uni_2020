def solution(arr):
    num_same = 1
    max_num = 1
    for i in range(1, (len(arr))):
        if arr[i - 1] == arr[i]:
            num_same += 1
        else:
            num_same = 1
        if num_same > max_num:
                max_num = num_same
    return max_num

