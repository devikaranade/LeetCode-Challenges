class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter_char = {}
        start = 0
        max_freq = 0
        longest_substring_len = 0

        for end in range(len(s)):
            counter_char[s[end]]=counter_char.get(s[end], 0)+1
            max_freq = max(max_freq, counter_char[s[end]])

            is_valid = (end+1-start-max_freq <= k)
            if not is_valid:
                counter_char[s[start]]-=1
                start+=1
            longest_substring_len = end+1-start
        return longest_substring_len