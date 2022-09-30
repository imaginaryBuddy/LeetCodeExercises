# Search Problems 
## 1. Binary Search 

### 278 First Bad Version 
[LeetCode Link][278]

Idea: to use binary search. Use two pointers and treat 1...n as an array. 

In the code, **I had written: why do we need to save ver?**

Consider the case:

<img src="https://user-images.githubusercontent.com/81760484/193189822-6472212c-e209-4f5f-b976-a72f31ca4821.jpg" alt="firstbadversion" width="30%"/>
We can see that on the last iteration, mid is not a bad version. So if we were to just return mid, then it will be the wrong answer. 

[278]: https://leetcode.com/problems/first-bad-version/description/
