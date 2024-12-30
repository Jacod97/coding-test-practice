class Sosu:
    def __init__(self, nums):
        self.nums = nums
        self.items = []

    def case(self):
        n = len(self.nums)
        for x in range(n - 2):
            for y in range(x + 1, n - 1):
                for k in range(y + 1, n):
                    self.items.append(self.nums[x] + self.nums[y] + self.nums[k])
        return self.items

    def is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def count_primes(self):
        return sum(1 for item in self.items if self.is_prime(item))

def solution(nums):
    s = Sosu(nums)
    s.case()
    return s.count_primes()