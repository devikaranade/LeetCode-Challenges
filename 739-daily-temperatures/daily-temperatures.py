class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0]*n
        stack = []
        for i, tmp in enumerate(temperatures):
            while stack and temperatures[stack[-1]]<tmp:
                prev = stack.pop()
                answer[prev]=i-prev
            stack.append(i)
        return answer
