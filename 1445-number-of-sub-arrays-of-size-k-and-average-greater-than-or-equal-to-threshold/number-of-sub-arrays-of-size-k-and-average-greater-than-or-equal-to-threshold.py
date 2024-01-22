class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        j = 0
        i = 0
        count = 0
        sum_window = 0  
        while j < len(arr):
            sum_window += arr[j]
            if j - i + 1 == k:
                average = sum_window / k
                if average >= threshold:
                    count += 1
                sum_window -= arr[i]  
                i += 1
            j += 1
        return count
    