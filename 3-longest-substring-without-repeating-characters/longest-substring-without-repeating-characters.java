class Solution {
    public int lengthOfLongestSubstring(String s) {
        int left=0;
        int right=0;
        int max = 0;
        Map<Character, Integer> freq= new HashMap<>();
        while(right<s.length()) {
            char ch = s.charAt(right);
            freq.put(ch, freq.getOrDefault(ch, 0)+1);
            while (freq.getOrDefault(ch,0)>1) {
                char ch_left = s.charAt(left);
                freq.put(ch_left, freq.get(ch_left)-1);
                left++;
            }
            max = Math.max(max, right - left + 1);
            right++;
 
        }
        return max;
    }
}