class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        ans = []
        n = len(nums)
        arr = sorted(nums)
        for i in range(n):
            low = 0
            high = len(arr) - 1
            while low < high:
                mid = (low+high)//2
                if arr[mid] < nums[i]:
                    low = mid + 1
                else:
                    high = mid
            ans.append(low)
        return ans
                
