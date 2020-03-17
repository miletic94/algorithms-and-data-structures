l = [10, 9, 1, 2, 3, 4, 5, 6, 7, 8]


def stack_or_q(l, k):
    count = 0
    count_s = 0
    count_q = 0
    while k > 0:
        if l[0] > l[-1]:
            count += l[0]
            l.remove(l[0])
        else:
            for i in range(0, k):
                count_s += l[i]
            for i in range(-1, -k-1, -1):
                count_q += l[i]
            if count_s > count_q:
                count += count_s
            else:
                count += count_q
            break
        k = k-1
    return count


print(stack_or_q(l, 6))
