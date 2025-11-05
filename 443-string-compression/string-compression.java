class Solution {
    public int compress(char[] chars) {
        int left=0;
        int right=0;
        while (right<chars.length){
            char ch = chars[right];
            int count=0;
            while (right<chars.length && chars[right] == ch ) {
                right+=1;
                count+=1;
            }
            chars[left]=ch;
            left+=1;
            if (count>1) {
                for (char c : String.valueOf(count).toCharArray()) {
                    chars[left++] = c;
                }
            }
        }
        return left;
    }
}