class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        for i in J:
            if(i in S):
                count +=S.count(i)
        return count
                
                
                
        