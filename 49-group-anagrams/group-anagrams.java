class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> map=new HashMap<>();

        for (int i=0;i<strs.length;i++) {
            int[] freq = new int[26];

            for (char c:strs[i].toCharArray()){
                freq[c-'a']++;
            }

            StringBuilder sb=new StringBuilder();
            for(int f: freq) {
                sb.append(f).append('#');
            } 

            String key=sb.toString();
            map.computeIfAbsent(key, k->new ArrayList<>()).add(strs[i]);
        }
        return new ArrayList<>(map.values());
    }

}