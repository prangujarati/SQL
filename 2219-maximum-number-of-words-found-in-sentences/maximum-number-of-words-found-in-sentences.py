class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_words = 0
        for i in sentences:
            words = len(i.split(" "))
            max_words = max(words,max_words)
        return max_words
        