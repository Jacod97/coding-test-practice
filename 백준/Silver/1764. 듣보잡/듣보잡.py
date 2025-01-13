n,m = map(int, input().split()) # 앞의 글자는 n, 뒤의 글자는 m으로 할당됨.
n_set = set()
m_set = set()
for _ in range(n):
    n_set.add(input())
for _ in range(m):
    m_set.add(input())

def backjoon(x,y):
    return sorted(list(x&y))

print(len(backjoon(n_set,m_set)))
print('\n'.join(backjoon(n_set,m_set)))