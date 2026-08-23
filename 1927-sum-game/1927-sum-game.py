class Solution:
    def sumGame(self, num: str) -> bool:
        mid = len(num)//2
        firsthalf = 0
        secondhalf = 0
        q1 = 0
        q2 = 0
        for i in range(len(num)):
            if i < mid:
                if num[i].isdigit():
                    firsthalf+=int(num[i])
                else:
                    q1+=1
            else:
                if num[i].isdigit():
                    secondhalf+=int(num[i])
                else:
                    q2+=1
        diff = firsthalf-secondhalf
        if (q1+q2)% 2 == 1:
            return True
        return (q2-q1) * 9//2 != diff