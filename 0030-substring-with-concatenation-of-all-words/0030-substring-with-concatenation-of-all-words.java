class Solution {
    public List<Integer> findSubstring(String s, String[] words) {
        List<Integer> result = new ArrayList<>();
        if (s == null || s.length() == 0 || words == null || words.length == 0) {
            return result;
        }
        
        int wordLength = words[0].length();
        int totalLength = wordLength * words.length;
        
        Map<String, Integer> wordFreqMap = new HashMap<>();
        for (String word : words) {
            wordFreqMap.put(word, wordFreqMap.getOrDefault(word, 0) + 1);
        }
        
        for (int i = 0; i <= s.length() - totalLength; i++) {
            Map<String, Integer> tempMap = new HashMap<>(wordFreqMap);
            int j = i;
            while (j < i + totalLength) {
                String word = s.substring(j, j + wordLength);
                if (!tempMap.containsKey(word) || tempMap.get(word) == 0) {
                    break;
                }
                tempMap.put(word, tempMap.get(word) - 1);
                j += wordLength;
            }
            if (j == i + totalLength) {
                result.add(i);
            }
        }
        
        return result;
    }
}
