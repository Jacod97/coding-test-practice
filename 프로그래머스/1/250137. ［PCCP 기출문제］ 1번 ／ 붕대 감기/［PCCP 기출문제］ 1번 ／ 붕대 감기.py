def solution(bandage, health, attacks):
    hp = health
    flag = True
    heal_count = 0
    attack_count = len(attacks)
    
    for time in range(attacks[-1][0]+1):
        if time == attacks[-attack_count][0]:
            flag = False
            
        if flag:
            hp += bandage[1]
            heal_count += 1
            if heal_count == bandage[0]:
                hp += bandage[2]
                heal_count = 0
            if hp > health:
                hp = health
        else:
            hp -= attacks[-attack_count][1]
            attack_count -= 1
            heal_count = 0
            flag = True
            if hp <= 0:
                return -1
        # print(f"time:{time} hp:{hp} flag:{flag} hc:{heal_count}")
    return hp
# bandage = [시전 시간, 초당 회복량, 추가 회복량]
# health = 최대 체력
# attacks = [공격 시간, 피해량]