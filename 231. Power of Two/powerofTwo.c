bool isPowerOfTwo(int n){
    //Take care of edge case, if the number is less than or equal to 0 return false
    if (n <= 0) return false;
    
    //If not, return not n&n-1
    return !(n&(n-1));
    
    //Explanation:
    //In binary, all powers of two will only contain one 1
    //For example, 4 is represented as 0100. 
    //0100 -1 flips the digits to 1011
    //0100 & 1011 == 0000 due to propositional logic
    //!0000 = 1111 == true, else false

}
