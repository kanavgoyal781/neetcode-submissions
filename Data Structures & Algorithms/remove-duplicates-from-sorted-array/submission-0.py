class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 1
        if len(nums)==2 and nums[0]==nums[1]:
            return 1
        if len(nums)==2 and nums[0]!=nums[1]:
            return 2
        length=len(nums)
        i,j=1,1
        while i<length:
            if nums[i]==nums[i-1]:
                pass
            else:
                nums[j]=nums[i]
                j=j+1
            i=i+1
        return j


        