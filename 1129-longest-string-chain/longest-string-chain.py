class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        if len(words) == 1:
            return 1

        words.sort(key=lambda x: len(x))
        graph = defaultdict(list)
        indeg = defaultdict(int)
        n = len(words)
        indeg[words[0]] = 0

        for idx in range(1, n):
            word2 = words[idx]
            indeg[word2] = 0
            for j in range(idx - 1, -1, -1):
                if len(words[j]) < len(word2) - 1:
                    break
                if len(words[j]) == len(word2):
                    continue 
                
                if self.can_form_chain(words[j], word2):
                    graph[words[j]].append(word2)
                    indeg[word2] += 1
        
        queue = deque()
        for word in indeg:
            if indeg[word] == 0:
                queue.append(word)
        
        for key, value in graph.items():
            print(key, value)
        
        level = 0
        print(queue)
        while queue:
            ele = len(queue)
            while ele > 0:
                word = queue.popleft()
                for nei in graph[word]:
                    indeg[nei] -= 1
                    if indeg[nei] == 0:
                        queue.append(nei)
    
                ele -= 1
            level += 1
        
        return level
    
    def can_form_chain(self, word1, word2):
        if len(word2) != len(word1) + 1:
            return False
        
        if word2[0] + word1 == word2:
            return True
        
        if word1 + word2[-1] == word2:
            return True

        for idx in range(1, len(word2)-1):
            sample = word1[:idx] + word2[idx] + word1[idx:] 
            if sample == word2:
                return True
        
        return False
        