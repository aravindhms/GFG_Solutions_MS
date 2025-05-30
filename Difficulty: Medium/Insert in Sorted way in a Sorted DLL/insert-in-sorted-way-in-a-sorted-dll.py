#User function Template for python3

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class Solution:
    #Function to insert a node in a sorted doubly linked list.
    def sortedInsert(self, head, x):
        temp = head
        new = Node(x)
        # Add at the Beginning
        if temp.data >= x:
            temp.prev = new
            new.next = temp
            head = new
            return head
        else:
            while temp.data <= x and temp.next:
                temp = temp.next
            #Add at last
            if temp.next is None and temp.data < x :
                temp.next = new
                new.prev = temp
                return head
            #Add in the middle    
            temp.prev.next = new
            new.prev = temp.prev
            temp.prev = new
            new.next = temp
            return head


#{ 
 # Driver Code Starts
class Node:

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


def print_list(head):
    current = head
    while current:
        print(current.data, end=' ')
        current = current.next
    print()


if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        values = list(map(int, input().strip().split()))
        head = None
        tail = None

        for value in values:
            if head is None:
                head = Node(value)
                tail = head
            else:
                tail.next = Node(value)
                tail.next.prev = tail
                tail = tail.next

        value_to_insert = int(input().strip())
        solution = Solution()
        head = solution.sortedInsert(head, value_to_insert)
        print_list(head)

        print("~")

# } Driver Code Ends