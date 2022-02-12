class Solution {
    public boolean isPalindrome(String s) {
        //Make an empty string to put the alphanumeric chars
        String mystring = "";
        
        for (char c : s.toCharArray()){
            if (Character.isDigit(c) || Character.isLetter(c)){
                mystring += c;
            }
        }
        //Make mystring lowercase
        mystring = mystring.toLowerCase();
        
        //Use a pointer at the beginning and the end
        int pointerA = 0;
        int pointerB = mystring.length()-1;
        
        //While the two pointers do not cross, check if the chars are equal and return the result
        while(pointerA<=pointerB){
            if (mystring.charAt(pointerA++) != mystring.charAt(pointerB--)){
                return false;
            }
        }
        return true;
    }
}