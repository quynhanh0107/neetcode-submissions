class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums: 
            id = abs(num) - 1
            if nums[id] < 0: 
                return abs(num)
            nums[id] *= -1
        return -1