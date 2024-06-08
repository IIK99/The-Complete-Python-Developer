some_list = ["a", "b", "c", "b", "d", "m", "n", "n"]
print(list(set([i for i in some_list if some_list.count(i) > 1])))

