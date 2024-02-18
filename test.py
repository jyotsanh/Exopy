def findMin(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_num  = nums[0]
        index = 0
        for i in range(len(nums)):
            if nums[i]<min_num:
                
                index = i
                
        return index
print(findMin([4,5,6,7,0,1,2]))
