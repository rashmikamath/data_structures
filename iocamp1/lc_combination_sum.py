def minSubArrayLen(target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        if target==None or nums==None:
            return 
        
        start = 0
        end = 0
        sum_val = nums[0] 
        
        res = []
        while start < len(nums):
            # if start > end:
            #     start = end
            #     sum_val = nums[start]
            if sum_val < target:
                if end == len(nums)-1:
                    break
                end += 1
                sum_val += nums[end]
                
            elif sum_val > target:
                sum_val -=  nums[start]
                start += 1
            else: 
                return(start,end)
        return None
minSubArrayLen(7, [2,3,1,2,4,3])