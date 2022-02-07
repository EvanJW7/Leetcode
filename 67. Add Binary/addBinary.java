class Solution {
    public String addBinary(String a, String b) {
        //Make a string builder to be able to make a string
        StringBuilder sb = new StringBuilder();
        //Create two variables to traverse String a and String b. Start at the end
        int i = a.length()-1;
        int j = b.length()-1;
        
        //Make a variable called carry that is initialized to 0
        int carry = 0;
        
        //Iterate through the two binary numbers
        while(i >= 0 || j >= 0){
            int sum = carry;
            if(i >= 0) sum += a.charAt(i)-'0';
            if(j >= 0) sum += b.charAt(j)-'0';
            //Append the sum mod two which will always get a 1 or a 0 in this case
            sb.append(sum%2);
            //Divide the sum 2 (integer division)
            carry = sum/2;
            //Decrement the i and j pointers
            i--;
            j--;
        }
        //In some cases we may end up with an extra zero, so make sure to add it to the sb
        if (carry != 0) sb.append(carry);
        //Return a reverse of our string builder since it is in reverse order
        return sb.reverse().toString();
    }
}