# 첫째 줄: 듣도 못한 사람의 수 N, 보도 못한 사람의 수 M
N, M = map(int, input().split())

# 듣도 못한 사람의 명단을 set에 저장
not_heard = set()
for _ in range(N):
    not_heard.add(input().strip())

# 보도 못한 사람의 명단을 set에 저장
not_seen = set()
for _ in range(M):
    not_seen.add(input().strip())

# 두 집합의 교집합 구하기
result = sorted(not_heard & not_seen)

# 결과 출력
print(len(result))
print('\n'.join(result))