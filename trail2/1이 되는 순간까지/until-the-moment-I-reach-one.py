def func(n, a):
    if n == 1:
        return a
    if n % 2 == 0:
        return func(n // 2, a + 1)
    else:
        return func(n // 3, a + 1)


N = int(input())
print(func(N, 0))