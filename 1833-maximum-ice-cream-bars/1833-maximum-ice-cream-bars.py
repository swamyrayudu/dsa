class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        count = 0
        sumi = 0
        for i in range(len(costs)):
            sumi+=costs[i]
            if sumi <= coins:
                count+=1
            else:
                break
        return count
