class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        #Make an empty list to append to later
        uncommons = []
        #Split the sentences by word so you can compare them
        s1 = s1.split()
        s2 = s2.split()
        #Check both sentences. If the count is 1 and it isn't in the other, append it to uncommons
        for word in s1:
            if s1.count(word) == 1 and word not in s2:
                uncommons.append(word)
        for word in s2:
            if s2.count(word) == 1 and word not in s1:
                uncommons.append(word)
        #Return list of uncommon words
        return uncommons 
        