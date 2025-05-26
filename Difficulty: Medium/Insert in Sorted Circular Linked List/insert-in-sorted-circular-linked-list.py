
class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None

class Solution:
    def sortedInsert(self, head, data):
        new_node=Node(data)
        if head is None:
            new_node.next=new_node
            return new_node
        ptr=head
        cur=head
        prev=None
        while(ptr.next!=cur):
            ptr=ptr.next
        if head.data>=data:
            new_node.next=head
            head=new_node
            ptr.next=head
            return head
        while(cur.data<=data and cur!=ptr):
            prev=cur
            cur=cur.next
        if cur!=ptr:
            prev.next=new_node
            new_node.next=cur
        elif cur.data>=data:
            prev.next=new_node
            new_node.next=cur
        else:
            ptr.next=new_node
            new_node.next=head
        return head