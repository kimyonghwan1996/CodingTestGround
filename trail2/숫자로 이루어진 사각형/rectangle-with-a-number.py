n = int(input())
m = 0
for _ in range(n):
    for _ in range(n):
        m += 1
        if m >= 10:
            m = 1
        print(m, end=" ")
    print("")
# for i in range(n):
#     for j in ra
# Please write your code here.