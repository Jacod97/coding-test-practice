def solution(s, skip, index):
    # skip에 포함되지 않은 알파벳 리스트 생성
    alphabet = [ch for ch in 'abcdefghijklmnopqrstuvwxyz' if ch not in skip]

    result = ""
    for ch in s:
        # 현재 문자의 위치를 찾음
        cur_idx = alphabet.index(ch)
        # index만큼 이동 (순환)
        new_idx = (cur_idx + index) % len(alphabet)
        result += alphabet[new_idx]

    return result
