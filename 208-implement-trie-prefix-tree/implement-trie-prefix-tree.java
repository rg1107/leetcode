class Trie {

    private TrieNode root;

    public Trie() {
        root = new TrieNode('0', false);
    }
    
    public void insert(String word) {
        int n = word.length();
        TrieNode temp = root;
        for (int index = 0;index < n; index++) {
            char ch = word.charAt(index);
            if (temp.nextChars[ch - 'a'] == null) {
                temp.nextChars[ch - 'a'] = new TrieNode(ch, false);
            }
            temp = temp.nextChars[ch - 'a'];
        }
        temp.isEndOfWord = true;
    }
    
    public boolean search(String word) {
        int n = word.length();
        TrieNode temp = root;
        for (int index = 0;index < n; index++) {
            char ch = word.charAt(index);
            if (temp.nextChars[ch - 'a'] == null) {
                return false;
            }
            temp = temp.nextChars[ch - 'a'];
        }
        return temp.isEndOfWord;
    }
    
    public boolean startsWith(String prefix) {
        int n = prefix.length();
        TrieNode temp = root;
        for (int index = 0;index < n; index++) {
            char ch = prefix.charAt(index);
            if (temp.nextChars[ch - 'a'] == null) {
                return false;
            }
            temp = temp.nextChars[ch - 'a'];
        }
        return true;
    }

    class TrieNode {
        char val;
        boolean isEndOfWord;
        TrieNode[] nextChars;

        public TrieNode(char val, boolean isEndOfWord) {
            this.val = val;
            this.isEndOfWord = isEndOfWord;
            this.nextChars = new TrieNode[26];
        }
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */