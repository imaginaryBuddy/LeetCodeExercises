# Dynamic Programming 
- Used when there are dependent, overlapping subproblems. 
- When there is a sequence of decisions to be made [(quoted from Abdul Bari)][1]
- When solving optimization problems. 
- A combination of recursion and memoization 

memoization
: an optimization technique used primarily to speed up computer programs by storing the results of expensive function calls and returning the cached result when the same inputs occur again. - Wikipedia

## Some Important Concepts 

### 1. 1/0 Knapsack Problem 
You are a thief, and you want to steal the items such that you maximize the total profit that the items give. The 1/0 comes from the fact that you can only include/ exclude the item. 

- Problem statement: What is the maximum profit P that can be obtained given that:
  - the knapsack has a maximum capacity `m`
  - you have `n` objects to choose from
  - the profits for each respective item 1,2,...,n is given as `pi = {p1, p2,..., pn}`
  - the weights for each respective item given as `wi = {w1, w2,..., wn}`

#### Naive Approach? 
- Find the profit of each possible combination, provided that the solution obeys the capacity constraint `m` and the 1/0 concept. 

* this takes O(2^n), as there are 2^n considerations/ possible combinations, (for each item you either include or exclude, you make a binary decision, so 2 * 2 * 2 * 2..., n times.)

#### DP Approach, using tabulation 
Note that: these are merely my notes, and I have added some additional notes to clear my own doubts. I had followed the youtube video by Abdul Bari (linked in Reference). 

<img src = "https://user-images.githubusercontent.com/81760484/193446350-e34a9e42-43c1-4d8a-b1b8-da4cb11d625c.jpg" width="50%" />
<img src = "https://user-images.githubusercontent.com/81760484/193446353-76e99187-940f-49af-80ea-c55e4378d06b.jpg" width="50%" />
<img src = "https://user-images.githubusercontent.com/81760484/193446355-bfb5bacd-6945-4f12-9bbc-df525ffaee3a.jpg" width="50%" />


# Reference
https://www.youtube.com/watch?v=nLmhmB6NzcM

[1]: https://www.youtube.com/watch?v=nLmhmB6NzcM
