class Solution {
    public boolean isSubsequence(String s, String t) {
        //Throw in this edge case or we will get a security manager error
        if (s.equals("")){
            return true;
        }
        
        //Initialize i to 0, loop through the t string with j intialized to 0
        int i = 0;
        for (int j = 0; j<t.length(); j++){
            //If i char is equal to j char, increment i. J is automatically incremented no matter what
            if (s.charAt(i) == t.charAt(j)){
                i++;
            }
        //When we get to the end of the iterations, i should be equal to s.length
        if (i == s.length()){
            return true;
            }
        }
        return false; 
    }
}

