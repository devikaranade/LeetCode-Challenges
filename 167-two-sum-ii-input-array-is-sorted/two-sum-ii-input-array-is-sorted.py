class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        h = {}
        for i in range(len(numbers)):
            diff = target-numbers[i] # 9-2 = 7
            if diff not in h:
                h[numbers[i]] = i+1 #h[0] = 2
            else:
                return h[diff], i+1
        



        # for i in range(0, len(numbers)):
        #     for j in range(i+1, len(numbers)):
        #         if numbers[i]+numbers[j]==target:
        #             print(i,j)
        #             return [i+1, j+1]
                
            
            


        