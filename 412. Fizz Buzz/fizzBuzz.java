class Solution {
    public List<String> fizzBuzz(int n) {
        //Create empty String ArrayList
        List<String> myList = new ArrayList<>();
        //Iterate with i, as long as i is less than n. Use 15 to speed up code
        for (int i = 1; i<=n; i++){
            if (i%15 == 0){
                myList.add("FizzBuzz");
            }
            else if (i%3 == 0){
                myList.add("Fizz");
            }
            else if (i%5 == 0){
                myList.add("Buzz");
            }
            else{
                myList.add(String.valueOf(i));
            }
        }
        return myList;
    }
}
