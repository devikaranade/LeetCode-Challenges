class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_sum = 0
        step = 0
        for i in range(len(gain)):
            step+=gain[i]
            if step>max_sum:
                max_sum=step
        return max_sum