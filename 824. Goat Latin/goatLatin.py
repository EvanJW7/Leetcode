class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        '''
        Logic - Loop through each word in the sentence. Check to see if the first letter in each 
        word is a vowel. If it is, change the word to match the problem description and add it to 
        our newString. Make sure to increment a each time. Must start at 2.
        '''
        a = 2
        newString = ""
        for word in sentence.split():
            if word[0].lower() in 'aeiou':
                word += 'm' + 'a'*a
            else:
                word = word[1:] + word[0] + 'm' + 'a'*a
            
            newString += word + ' '
            a += 1
            
        #Cut off the last ending space in newString before returning     
        return newString[:-1]