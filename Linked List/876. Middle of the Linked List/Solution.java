
  //Definition for singly-linked list.
class ListNode {

    public int val;
    public ListNode next;

    public  ListNode() {}
    public  ListNode(int val) { 
        this.val = val;
     }
    public ListNode(int val, ListNode next) { 
        this.val = val; 
        this.next = next; 
    }
 }


class Solution {
    public ListNode middleNode(ListNode head) {
        ListNode returnList = new ListNode(head.val, head.next);
        ListNode currentNode = new ListNode(head.val, head.next);
        while(currentNode.next != null){
            returnList = returnList.next;
            if (currentNode.next.next == null) currentNode = currentNode.next;
            else currentNode = currentNode.next.next; 
        }
        return returnList;
    
    }
}