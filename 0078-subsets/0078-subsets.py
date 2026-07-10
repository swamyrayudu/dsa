class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        arr = []
        def f(i,li):
            if i == n:
                arr.append(li.copy())
                return
            li.append(nums[i])
            pick = f(i+1,li)
            li.pop()
            not_pick = f(i+1,li)
        f(0,[])
        return arr