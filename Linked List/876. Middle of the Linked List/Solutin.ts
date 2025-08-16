
 /** Definition for singly-linked list. **/ 
  class ListNode {
      val: number
      next: ListNode | null
     constructor(val?: number, next?: ListNode | null) {
         this.val = (val===undefined ? 0 : val)
         this.next = (next===undefined ? null : next)
     }
  }
 

function middleNode(head: ListNode | null): ListNode | null {
    var returnNode : ListNode | null  = head;
    var currentNode : ListNode | null = head;

    while(currentNode?.next){
        returnNode = returnNode!.next;
        if(currentNode.next.next == null) currentNode = currentNode.next;
        else currentNode = currentNode.next.next;
    }
    return returnNode;
    
};