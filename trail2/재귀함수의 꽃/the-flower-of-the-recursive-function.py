N = int(input())

def func(n):
    if n == 0:
        return
    print(n, end=" ")
    func(n - 1)

def func2(n):
    if n == 0:
        return
    func2(n-1)
    print(n, end=" ")
func(N)
func2(N)
# Please write your code here.