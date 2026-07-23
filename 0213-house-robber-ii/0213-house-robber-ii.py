class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * (n+1)
        dp2 = [-1] * (n+1)
        def f(i,arr,dp):
            if i == len(arr) -1:
                return arr[i]
            if len(arr) <= i:
                return 0
            if dp[i] != -1:
                return dp[i]
            not_pick = 0 + f(i+1,arr,dp)
            pick = arr[i] + f(i+2,arr,dp)
            dp[i] = max(not_pick,pick)    
            return dp[i]  
        if len(nums) <= 1:
            return nums[0]    
        nums1 = nums[:-1]
        nums2 = nums[1:]
        return max(f(0,nums1,dp),f(0,nums2,dp2))