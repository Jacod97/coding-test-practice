import math

def dasom(num):
    room = str(num)
    plastic = [i for i in room]
    plastic_set = {}

    for i in plastic:
        if i == '6' or i == '9':
            plastic_set[i] = math.ceil((plastic.count('6') + plastic.count('9'))/2)
        else:
            plastic_set[i] = plastic.count(i)

    return max(plastic_set.values())

print(dasom(input()))