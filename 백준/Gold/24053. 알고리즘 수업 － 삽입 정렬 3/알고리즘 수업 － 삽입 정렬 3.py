n = int(input())
arrA = list(map(int, input().split()))
arrB = list(map(int, input().split()))

def insert_sort(n,arrA,arrB):
    answer = []
    for i in range(n):
        strong = arrA.index(max(arrA[:n-i]))
        while strong != n-i-1:
            answer.append(arrA.copy())
            weak = arrA[strong+1]
            arrA[strong+1] = arrA[strong]
            answer.append(arrA.copy()) # 여기서 한번 저장
            if strong >= 1:
                for x in range(strong):
                    arrA[strong-x] = max(arrA[strong-x-1], weak)
                    answer.append(arrA.copy()) # 여기서 한번 더 저장
                    arrA[strong-x-1] = min(arrA[strong-x-1], weak)
                    if arrA == sorted(arrA):
                        answer.append(arrA)
                        break
            else:
                arrA[strong] = weak
            strong += 1
        
    if arrB in answer:
        return 1
    else:
        return 0
    
print(insert_sort(n,arrA,arrB))
