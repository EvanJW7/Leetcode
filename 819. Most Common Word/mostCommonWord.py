class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        #Remove punctuation from the paragraph 
        for punct in ".,;,:,?,!,'":
            paragraph = paragraph.replace(punct, ' ')
        #Make paragraph lowercase and split it
        paragraph = paragraph.lower().split()
        #Take the brackets off of the banned word
        banned = str(' '.join(banned))
        #Make an empty list and append all the words from the original paragraph that aren't banned
        newParagraph = []
        for word in paragraph:
            if word not in banned:
                newParagraph.append(word)
        #Make a dictionary of word frequencies
        data = { }
        for word in newParagraph:
            if word not in data: 
                data[word] = 1
            else:
                data[word] += 1
        #Find the word with the most occurances 
        x = max(data, key = data.get)
        #Return it in string form 
        return str(x)
    
    
    