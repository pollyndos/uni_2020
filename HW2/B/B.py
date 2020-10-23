def solution(x):
    first_ind = 0
    last_ind = 0
    new_list = list(x)
    # find index of the first 'H' or 'h'
    for i in range(len(new_list)):
        if new_list[i] == 'h' or new_list[i] == 'H':
            first_ind = i
            break
    # find index of the last 'H' or 'h' (the first from the end)
    for i in range(len(new_list)):
        new_list_reversed = new_list[::-1]
        if new_list_reversed[i] == 'h' or new_list[i] == 'H':
            # we find the real index
            last_ind = len(new_list) - i - 1
            break
    # now we search for 'h'/'H' between the first and las indices
    for i in range(first_ind + 1, last_ind):
        if new_list[i] == 'h':
            new_list[i] = 'H'
            
    new_list = ['one' if x == '1' else x for x in new_list]
    new_list = [new_list[x] for x in range(len(new_list)) if x == 0 or x % 3 != 0 ]
    return ''.join(new_list)

