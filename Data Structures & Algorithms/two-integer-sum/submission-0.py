class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for key, value in enumerate(nums):
            rem = target - value
            if rem in seen:
                return [seen[rem],key]
            if value not in seen:
                seen[value] = key
        return [0,0]