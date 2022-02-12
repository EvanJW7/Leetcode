class Solution:
    def capitalizeTitle(self, title: str) -> str:
        #Make an empty output string to add to later
        output = ""
        #Iterate through the words in title. Make sure to split 
        for word in title.split():
            if len(word)<= 2:
                word = word.lower() + ' '
            else:
                word = word.title() + ' '
            output += word
        #Return output with the last char chopped off because it is a space
        return output[:-1]