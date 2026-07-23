class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        counter = 1
        for i in range(len(nums) - 1):
            if int(nums[i]) == int(nums[i+1]):
                counter = 2
            else:
                continue
        if counter ==2:
            return True
        else:
            return False