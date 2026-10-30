class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        aset = set()
        for n in nums:
            if n in aset:
                return True
            else:
                aset.add(n)
        return False