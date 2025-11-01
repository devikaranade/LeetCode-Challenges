class Solution {
    public double nthPersonGetsNthSeat(int n) {
        if (n==1) {
            return n;
        }
        return 0.5;
    }
}


//3 = .66%

// scenario 1 true
// 1 2 3

//[123,132,213,231,321,312] 
//[123,213,321,312] -> 2^n-1 / 2^n+1 = 4 = n/2^n-1

// scenario 2 true
// 2 1 3

// scenario 3 false
// 3 2 1

// scenario 4 false
// 2 3 1


//2^2 = 8