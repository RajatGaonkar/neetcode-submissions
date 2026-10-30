class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        curmax = arr[-1]
        arr[-1] = -1
        for i in range(len(arr)-2, -1, -1):
            i_elem = arr[i]
            arr[i] = curmax
            curmax = max(curmax, i_elem)
        return arr