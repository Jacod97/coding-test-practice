def numbers(arr, x):
    arr.sort() 
    left, right = 0, len(arr) - 1  
    count = 0

    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum > x:
            right -= 1 
        elif current_sum < x:
            left += 1 
        else:
            count += 1 
            left += 1
            right -= 1

    return count

# 입력 처리
n = int(input())
arr = list(map(int, input().split())) 
x = int(input())

print(numbers(arr, x))