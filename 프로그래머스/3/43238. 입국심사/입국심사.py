def solution(n, times):
    # 이분 탐색을 위한 초기 범위 설정
    left = 1
    right = max(times) * n  # 가장 느린 심사관이 모든 인원 처리하는 최악의 경우

    answer = right  # 최소 시간을 찾기 위해 최대값으로 초기화

    while left <= right:
        mid = (left + right) // 2  # 중간값 (예상 심사 시간)

        # mid 시간 동안 처리 가능한 총 인원 수 계산
        total = sum(mid // time for time in times)

        if total >= n:
            # n명 이상 처리 가능 → 더 짧은 시간에서도 가능한지 확인
            answer = mid
            right = mid - 1
        else:
            # n명 처리 불가능 → 더 많은 시간이 필요
            left = mid + 1

    return answer