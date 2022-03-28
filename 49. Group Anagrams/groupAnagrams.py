class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Make an anagrams dictionary to store anagrams
        anagrams = {}
        #Loop through the strs list
        for word in strs:
            sorted_word = "".join(sorted(word))
            #If the sorted version of the word is not in anagrams: add the original word as a value
            if sorted_word not in anagrams:
                anagrams[sorted_word] = [word]
            #If the sorted version is in the anagrams dictionary, append the version as an additional value
            else:
                anagrams[sorted_word].append(word)
        
        #Return a list of all the values in our anagrams dictionary
        return list(anagrams.values())
        