class MinStack {
    
    //Make a stack to put all the values
    Stack<Integer> mystack = new Stack();
    //Make a stack to put the minimum value
    Stack<Integer> min_value = new Stack();
    
    
    public void push(int val) {
        //If the min_value stack is empty or the int val is less than the top item on min_value:
        //Push the new value onto the min_value stack
        if (min_value.isEmpty() || val <= min_value.peek()){
            min_value.push(val);
        }
        //Else, push the val onto the stack of all values
        mystack.push(val);
        
    }
    
    public void pop() {
        //This block of code makes sure if we pop off the minimum value from mystack, 
        //it will also get removed from the min_value stack.
        if (mystack.peek().equals(min_value.peek())){
            min_value.pop();
        }
        mystack.pop();
        
    }
    
    public int top() {
        return mystack.peek();
        
    }
    
    public int getMin() {
        return min_value.peek();
        
        
    }
}