**Design**
- It's pretty straightforward in this case
- We have an a given array and a given x.
- We will loop through the list and compare x with every element in the list
- If one equals to x, then we're done. Otherwise, keep comparing until the end of the array.
- If we reach the end and can't find any, that means x is not in the list, therefore, return False

**Correctness**
- Initialization: Since the algorithm is simple and straightforward, we don't have to check anything before the first iteration of the loop.
- Maintenance: We go through each element in the loop one by one and check if one equals to x. 
- Termination: When the loop terminates, the invariant gives us True if there exists a element that equals to x and False if there's none.


**Efficiency**
- It's not efficient because we have to go through every element in the list until we reach the end. 
- The worst case scenario is when the item we need to find is the last element in the list, which is O(n)
- The best case scenario is when the item is the first element in the list, which is O(1)

**Testing**
- Testing is also straightforward. I have included it in my main program.
- If an item is in the list, expected output is True
- If an item is not in the list, expected output is False