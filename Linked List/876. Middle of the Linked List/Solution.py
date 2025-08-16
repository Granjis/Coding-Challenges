from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Case 1: Odd size linked list.
        current_middle_node = head #Variable to store  node that corresponds to the middle of the list.
        current_node = head #Variable to track the current node while traversing the Linked list.
        current_node_index = 1
        #We iterate through the linked list untill we find the last element.
        while current_node is not None:
            #While walking through the list, everytime the current position is even, we move the half of the list one node 
            # to the left.
            if current_node_index % 2 == 0:
                current_middle_node = current_middle_node.next # type: ignore
            current_node_index += 1
            current_node = current_node.next
        return current_middle_node
                
                
            
            
