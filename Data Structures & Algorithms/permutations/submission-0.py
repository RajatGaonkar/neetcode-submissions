class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        res = []
        perms = self.permute(nums[1:])
        for p in perms:
            for i in range(len(p)+1):
                p_c = p.copy()
                p_c.insert(i, nums[0])
                res.append(p_c)
        return res

