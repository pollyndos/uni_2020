def solution(total):
    hours = total // 60
    mins = total % 60
    if hours > 24:
        hours = hours % 24
    time = str(hours) + " " + str(mins)
    return time
