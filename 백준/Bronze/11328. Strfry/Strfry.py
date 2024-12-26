def is_possible(test_cases):
    results = []
    for word1, word2 in test_cases:
        if sorted(word1) == sorted(word2):
            results.append("Possible")
        else:
            results.append("Impossible")
    return results

# 테스트 입력 받기
n = int(input())  # 테스트 케이스 수
test_cases = [input().split() for _ in range(n)]

# 결과 출력
for result in is_possible(test_cases):
    print(result)