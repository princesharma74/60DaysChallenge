from itertools import combinations
lst = [2, 5, 9, 4]
for subset in combinations(lst, 2):
    print(subset)
