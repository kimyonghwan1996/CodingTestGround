n = int(input())
a = 1
def func(n):
    if 0 == n:
        return
    func(n-1)
    print(n, end=" ")

def func2(n):
    if 0 == n:
        return
    print(n, end=" ")
    func2(n-1)

func(n)
print()
func2(n)
    
# Please write your code here.