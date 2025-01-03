def solution(lottos, win_nums):
    lot_dict = {x: 7-x for x in range(1, 7)}
    lot_dict[0] = 6
    min_num = len([i for i in lottos if i in win_nums]) # 최악의 당첨 수
    bad = lot_dict[min_num]
    good = lot_dict[min_num + lottos.count(0)]
    answer = [good, bad]
    return answer