n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()
tf = True
c = 0
while tf and c < n:
    if A[c] != B[c]:
        tf = False
        break
    c += 1

if tf:
    print("Yes")
else:
    print("No")
# Please write your code here.