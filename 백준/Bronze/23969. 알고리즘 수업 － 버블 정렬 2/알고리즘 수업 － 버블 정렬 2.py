n, k = map(int, input().split())
li = list(map(int, input().split()))

for i in range(n - 1, 0, -1):
   for j in range(i):
      if li[j] > li[j + 1]:
         li[j], li[j + 1] = li[j + 1], li[j]
         k -= 1
         if k == 0:
            print(*li)
            exit()

print(-1)