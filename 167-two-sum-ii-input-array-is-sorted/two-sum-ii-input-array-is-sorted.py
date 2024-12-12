class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        h = {}
        for i in range(len(numbers)):
            diff = target-numbers[i] 
            if diff not in h:
                h[numbers[i]] = i+1 
            else:
                return h[diff], i+1
        