class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_count_map = Counter(words)
        len_word = len(words[0])
        res = []

        # outer loop is only length(word)
        # to indicate that if a word is left out from the start
        # and we want to still find the complete permuatation in the remaining part of string
        for low in range(len_word):
            start = low
            window = defaultdict(int)
            words_used = 0

            # Main finding inside of this loop
            for high in range(low, len(s) - len_word + 1, len_word):
                # directly incrementing by len(word) start since 
                # even if we didn't the find it in this iteration
                # we will find something when we start again from idx 1 and do the same procedure
                curr_word = s[high : high + len_word]

                # first form a word that actually exists
                # if not formed, shifting of the window
                if curr_word not in word_count_map:
                    # directly incrementing by len(word) start since 
                    # even if we didn't the find it in this iteration
                    # we will find something when we start again from idx 1 and do the same procedure
                    start = high + len_word

                    # also in this case we need to reinit everything...
                    window = defaultdict(int)
                    words_used = 0
                    continue
                
                words_used += 1
                window[curr_word] += 1
            
                # now word exists
                # but the frequecy is more
                # then also shift window
                # but shift by len(word) directly
                while window[curr_word] > word_count_map[curr_word]:
                    # remove an older word
                    # In Example 3
                    # when barfoofoo -> bar count is reduced from window
                    # and start is updated to 1st foo
                    window[s[start : start + len_word]] -= 1
                    words_used -= 1
                    start += len_word

                if words_used == len(words):
                    res.append(start)
            
        return res
        