class Solution {
    private boolean ifAnagram(String str1, String str2){
        if (str1.length() != str2.length()) return false;
        
        int[] count = new int[26];
        for (char c : str1.toCharArray()) {
            count[c - 'a']++;
        }
        for (char c : str2.toCharArray()) {
            if (count[c - 'a'] == 0) return false;
            count[c - 'a']--;
        }
        return true;
    }

    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> res = new ArrayList<>();
        Map<String, List<String>> map = new HashMap<>();
        
        for (String str : strs) {
            char[] chars = str.toCharArray();
            Arrays.sort(chars);
            String sorted = new String(chars);
            
            if (!map.containsKey(sorted)) {
                map.put(sorted, new ArrayList<>());
            }
            map.get(sorted).add(str);
        }
        
        for (List<String> list : map.values()) {
            res.add(list);
        }
        
        return res;
    }
}