def solution(n):
    if n != 0:
        z = "   _~_   " * n + '\n' +"  (o o)  " * n + '\n' + " /  V  \ " * n \
            + '\n' + "/(  _  )\\" * n  + '\n' + "  ^^ ^^  " * n
    else:
        z = ''
    return z
