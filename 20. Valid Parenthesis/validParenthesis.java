class Solution {
    public boolean isValid(String s) {
        //Make an empty stack
        Stack<Character> stack = new Stack();
        //Iterate through s and push or pop the stack
        for (char c : s.toCharArray()){
            if (c == '[' || c == '(' || c == '{'){
                stack.push(c);
            }
            else if( c == ']' && !stack.isEmpty() && stack.peek() == '['){
                stack.pop();
            }
              else if( c == ')' && !stack.isEmpty() && stack.peek() == '('){
                stack.pop();
            }
              else if( c == '}' && !stack.isEmpty() && stack.peek() == '{'){
                stack.pop();
            }
            else{
                return false;
            }
                
            }
        //Return a boolean if the stack is empty or not
        return stack.isEmpty();
        }
    }
    