

def list_squared(m, n):
    test_numbers = [i for i in range(m, n)]
    answer = []
    for i in test_numbers:
        tple = []
        divisors = [j for j in range(1, i+1) if i % j == 0]
        if divisors:
            squared_divisors = [k ** 2 for k in divisors]
            for l in range(1, sum(squared_divisors) + 1):
                if l ** 2 == sum(squared_divisors):
                    tple.append(i)
                    tple.append(sum(squared_divisors))
                    answer.append(tple)

    return answer


print(list_squared(1, 250))