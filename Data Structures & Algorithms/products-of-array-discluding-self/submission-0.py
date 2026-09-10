class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_product = []
        prod = 1
        for i in nums:
            left_product.append(prod)
            prod *= i
        right_prod = 1
        for i in range(len(nums)-1,-1,-1):
            left_product[i] *= right_prod
            right_prod *= nums[i]
        return left_product    



        