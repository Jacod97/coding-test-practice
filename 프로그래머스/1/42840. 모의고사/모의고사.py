def solution(answers):
    # 수포자 No.1: 나는 간단하게 12345로 찍을게.^^
    supo1 = {1:1,2:2,3:3,4:4,0:5}
    # 수포자 No.2: ㅋㅋ 저 단순한 놈.. 나는 2번이니까 2랑 나머지 숫자를 번갈아서 찍는다.
    supo2 = {1:2,2:1,3:2,4:3,5:2,6:4,7:2,0:5}
    # 수포자 No.3: 니들은 예술을 몰라! 어디 보자... 나의 번호이자 행운의 숫자 3을 가장 먼저 찍고, 그 다음엔 나머지들로 찍어야겠다. 좀 허전하니까 2개씩 찍을까?
    supo3 = {1:3,2:3,3:1,4:1,5:2,6:2,7:4,8:4,9:5,0:5}

    # 이 3명의 byoungsin들은 0점을 맞아 마땅하나...
    st, nd, rd = 0, 0, 0

    # 관대하신 찍신께서 3명 모두에게 찍신의 가호를 내렸으니.
    answers.insert(0,0)
    for i in range(1, len(answers)):
        s, n, r = supo1[i%5], supo2[i%8], supo3[i%10]
        if s == answers[i]:
            st += 1
        if n == answers[i]:
            nd += 1
        if r == answers[i]:
            rd += 1

    bs = {1:st, 2:nd, 3:rd}  # ByoungSin: 1호, 2호, 3호
    bs_max = max(st, nd, rd)

    answer = []

    for i in range(1,4):
        if bs[i] == bs_max:
            answer.append(i)

    return answer