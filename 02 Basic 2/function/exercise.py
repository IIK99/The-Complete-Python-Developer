# highest even and odd numbers
def highest_number(li):
    even = []
    odd = []
    for i in li:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return max(even), max(odd)


print(highest_number([6, 7, 24, 11, 19, 25, 99, 88, 12]))
