def binary(val,n):
    result = []
    weights = [2**i for i in sorted(range(n), reverse=True)]
    for x in weights:
        if val >= x:
            result.append("1")
            val -= x
        else:
            result.append("0")
    return result

def solution(n,arr1,arr2):
    arr = []
    for i in range(n):
        memory = []
        first_map = binary(arr1[i],n)
        second_map = binary(arr2[i],n)
        for j in range(n):
            if int(first_map[j]) + int(second_map[j]) > 0:
                memory.append("#")
            else:
                memory.append(" ")
        arr.append(''.join(memory))

    return arr

    
