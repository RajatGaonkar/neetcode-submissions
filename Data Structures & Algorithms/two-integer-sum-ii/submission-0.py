class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hmap = {}
        for i, n in enumerate(numbers):
            left = target - n
            print(hmap)
            if (n in hmap.keys()):
                return [hmap[n]+1, i+1]
            hmap[left] = i