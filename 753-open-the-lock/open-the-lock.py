class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        next_slot = {
            "0": "1",
            "1": "2",
            "2": "3",
            "3": "4",
            "4": "5",
            "5": "6",
            "6": "7",
            "7": "8",
            "8": "9",
            "9": "0",
        }

        prev_slot = {
            "0": "9",
            "1": "0",
            "2": "1",
            "3": "2",
            "4": "3",
            "5": "4",
            "6": "5",
            "7": "6",
            "8": "7",
            "9": "8",
        }

        visited = set(deadends)
        q = deque()
        turns = 0

        if "0000" in visited:
            return -1
        
        q.append("0000")
        visited.add("0000")

        while q:
            n = len(q)
            for _ in range(n):
                curr = q.popleft()
                if curr==target:
                    return turns
                
                for wheel in range(4):
                    new_comb = list(curr)
                    new_comb[wheel]=next_slot[new_comb[wheel]]
                    new_comb_str = ''.join(new_comb)
                    if new_comb_str not in visited:
                        visited.add(new_comb_str)
                        q.append(new_comb_str)

                    new_comb = list(curr)
                    new_comb[wheel]=prev_slot[new_comb[wheel]]
                    new_comb_str = ''.join(new_comb)
                    if new_comb_str not in visited:
                        visited.add(new_comb_str)
                        q.append(new_comb_str)
            turns+=1
        return -1
                    


