class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if(len(nums)%2==0):
                len1 = len(nums)//2
        else:
            len1 = (len(nums)//2)+ 1
        for i in nums:            
            if(nums.count(i)>=len1):
                return i
            else:
                nums.remove(i)
                
                