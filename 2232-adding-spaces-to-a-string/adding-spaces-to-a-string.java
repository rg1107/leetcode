class Solution {
    public String addSpaces(String s, int[] spaces) {
        StringBuilder result = new StringBuilder("");
        int start = 0;

        for (int i=0;i<spaces.length;i++) {
            while (start < s.length() && start < spaces[i]) {
                result.append(s.charAt(start));
                start++;
            }
            result.append(" ");
        }

        while(start < s.length()) {
            result.append(s.charAt(start));
            start++;
        }

        return result.toString();
    }
}