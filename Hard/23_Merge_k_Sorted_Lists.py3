# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import queue

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = queue.PriorityQueue() 
        head = None
        currNode = None
        for i in range(len(lists)):
            # put all the first elements 
            if lists[i]: 
                minHeap.put((lists[i].val, id(lists[i]), lists[i]))

        while not minHeap.empty():
            # extract the smallest one 
            smallest = minHeap.get()[2]
            if head == None:
                head = smallest
                currNode = smallest
            else:
                prev = currNode 
                prev.next = smallest
                currNode = smallest 
            
            if smallest.next:
                minHeap.put((smallest.next.val, id(smallest.next), smallest.next))
            

        return head
