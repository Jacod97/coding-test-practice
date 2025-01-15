n,k = map(int,input().split())
array = list(map(int,input().split()))

def choice_sort2(n,k,array):
    index = array.index(max(array))
    count = 0
    while n > 1:
        if index != n-1:
            array[index],array[n-1] = array[n-1],array[index]
            n -= 1
            index = array[:n].index(max(array[:n]))
            count += 1
        else:
            n -= 1
            index = array[:n].index(max(array[:n]))

        if count == k:
            break

    if count < k:
        return -1
    array = [str(i) for i in array]
    return ' '.join(array)
print(choice_sort2(n,k,array))