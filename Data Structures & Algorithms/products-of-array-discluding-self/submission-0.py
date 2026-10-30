class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        output = [1]*len(nums)
        for i in range(len(nums)):
            output[i] = pre
            pre *= nums[i]
        post = 1
        for i in range(len(nums)-1, -1, -1):
            output[i] *= post
            post *= nums[i]
        return output