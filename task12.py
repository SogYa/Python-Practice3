def catalan(n):
    c = 0
    if n == 0:
        return 1
    else:
        for i in range(n):
            c += catalan(i) * catalan(n - i - 1)
        return c


print(catalan(10))