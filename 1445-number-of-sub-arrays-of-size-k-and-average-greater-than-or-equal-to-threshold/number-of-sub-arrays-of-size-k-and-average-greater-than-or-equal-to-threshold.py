class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # if threshold==0:
        #     return len(arr)-k+1
        # j = 0
        # i = 0
        # count = 0
        # list1 = []
        # while j<len(arr):
        #     ws = j-i+1
        #     list1.append(arr[j])
        #     if ws==k:
        #         if (sum(list1)/k)>=threshold:
        #             count+=1
        #         list1 = list1[1:]
        #         i+=1
        #     j+=1
        # return count

        j = 0
        i = 0
        count = 0
        sum_window = 0  # Variable to keep track of the sum of the current window
        while j < len(arr):
            sum_window += arr[j]

            if j - i + 1 == k:
                average = sum_window / k
                if average >= threshold:
                    count += 1
                sum_window -= arr[i]  # Move the window by removing the leftmost element
                i += 1

            j += 1

        return count
                    
                



        