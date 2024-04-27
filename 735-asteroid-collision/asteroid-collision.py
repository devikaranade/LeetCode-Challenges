class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in asteroids:
            if i>0:
                stack.append(i) # stack = [5,10]
            else:
                while stack and stack[-1]>0:
                    if stack[-1]+i==0:
                        stack.pop()
                        break
                    if stack[-1]+i<0:
                        stack.pop()
                        continue
                    else:
                        break
                else:stack.append(i)
        return stack
