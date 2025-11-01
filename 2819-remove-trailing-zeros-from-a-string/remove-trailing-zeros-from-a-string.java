class Solution {
    public String removeTrailingZeros(String num) {
        int endInd = num.length() - 1;
        for (int i = num.length() - 1; i >= 0; i--) {
            if (num.charAt(i) - '0' == 0) {
                endInd--;
            } else {
                return num.substring(0, endInd+1);
            }
        }
        return num.substring(0, endInd);
    }
}