class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return []

        letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(idx,path):
            if len(path)==len(digits):
                comb.append("".join(path))
                return 
            poss_letters = letters[digits[idx]]
            for letter in poss_letters:
                path.append(letter)
                backtrack(idx+1, path)
                path.pop()
        comb = []
        backtrack(0, [])
        return comb