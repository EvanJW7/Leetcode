class Solution {
    public int lengthOfLastWord(String s) {
        //Split the string
        String[] words = s.split(" ");
        //Return the length of the index of the last word
        return (words[words.length-1].length());			
    }
}