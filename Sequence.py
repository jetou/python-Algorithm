def paixu(list):
    a = 0
    b = 0
    e = 0
    c = 1
    list_len = len(list)
    if list_len < 2:
        return list
    while b < (list_len-1):
        b += 1
        if b > 1:
                a += 1
                c += 1
        for i in range(c, list_len):
            if list[a] > list[i]:
                e = list[a]
                list[a] = list[i]
                list[i] = e

