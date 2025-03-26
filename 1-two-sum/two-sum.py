class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_dict = {}
        for i,num in enumerate(nums):
            diff = target - num
            if diff in num_dict:
                return [num_dict[diff],i]
            num_dict[num] = i
        return []
            
                

        