class Solution:
    def arrangeWords(self, text: str) -> str:
        split = text.split(" ")
        arr = [[word, idx, len(word)] for idx, word in enumerate(split)]
        arr.sort(key=lambda x: (x[2], x[1]))

        res = ' '.join([ele[0].lower() for ele in arr])
        return res.capitalize()
        