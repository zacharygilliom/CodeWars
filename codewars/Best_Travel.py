from itertools import combinations

def choose_best_sum(t, k, ls):
    sum_distances = 0
    lst = list(combinations(ls, k))
    highest_value = 0
    for x in lst:
        if sum(x) > highest_value and sum(x) <= t:
            highest_value = sum(x)
    if highest_value > 0:
        return highest_value
    else:
        return None


xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]

print(choose_best_sum(230,4,xs))
print(choose_best_sum(430,5,xs))
print(choose_best_sum(430,8,xs))