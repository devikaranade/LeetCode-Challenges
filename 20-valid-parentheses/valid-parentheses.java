class Solution {

    private static final Map<Character, Character> map = Map.of(
            '(', ')',
            '{', '}',
            '[', ']'
    );

    public boolean isValid(String s) {
        
        Stack<Character> stack=new Stack<>();
        
        for (int i=0;i<s.length();i++) {
            char c = s.charAt(i);

            if (map.containsKey(c)){
                stack.push(c);
            }
            else{
                if (stack.isEmpty()){
                    return false;
                }
                char ch = stack.pop();
                if (map.get(ch) != s.charAt(i)) {
                    return false;
                }
            }
        }
        return stack.isEmpty();
    }
}