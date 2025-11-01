class Solution {
    public String removeTrailingZeros(String num) {
        int endInd = num.length() - 1;
        for (; endInd >= 0; endInd--) {
            if (num.charAt(endInd) - '0' != 0) break;
        }
        return num.substring(0, endInd + 1);
    }
}