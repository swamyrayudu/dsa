class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        connect = nums + nums
        newsort = sorted(nums)
        for i in range(n):
            if connect[i:i+n] == newsort:
                return True
        return False
