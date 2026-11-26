N = int(input())


def func(n):
    if n == 0:
        return 0
    digit = n % 10
    return (digit**2) + func(n // 10)


print(func(N))