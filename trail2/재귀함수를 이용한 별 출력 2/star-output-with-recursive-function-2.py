n = int(input())


def print_stars(n):
  if n == 0:
    return

  # 1. 재귀 호출 전: n개부터 1개까지 줄어들며 출력
  print("* " * n)

  # 2. 다음 단계 호출
  print_stars(n - 1)

  # 3. 재귀 호출 후: 1개부터 n개까지 늘어나며 출력
  print("* " * n)


print_stars(n)