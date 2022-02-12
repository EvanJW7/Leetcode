class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        #All we have to do is set up a boolean
        return word == word.upper() or word == word.lower() or word == word.title()
