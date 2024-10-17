#User function Template for python3

class Node:
    def _init_(self, data):
        self.data = data
        self.next = None



class Solution:
    def alternatingSplitList(self, head):
        #Your code here
        if not head:
            return [None, None]

        # Initialize the two head pointers for the new lists
        list1 = head
        list2 = head.next

        # Pointers to build the new lists
        list1_current = list1
        list2_current = list2

        # Traverse the original list and split alternately
        current = head.next.next
        is_list1_turn = True  # Boolean to alternate between list1 and list2

        while current:
            if is_list1_turn:
                list1_current.next = current
                list1_current = list1_current.next
            else:
                list2_current.next = current
                list2_current = list2_current.next

            current = current.next
            is_list1_turn = not is_list1_turn  # Flip the boolean to alternate

        # Terminate the two lists
        list1_current.next = None
        list2_current.next = None

        return [list1, list2]

#{ 
 # Driver Code Starts
class Node:

    def __init__(self, x):
        self.data = x
        self.next = None


def printList(node):
    while node is not None:
        print(node.data, end=" ")
        node = node.next
    print()


if __name__ == "__main__":
    t = int(input().strip())

    for _ in range(t):
        arr = list(map(int, input().strip().split()))

        head = Node(arr[0])
        tail = head

        for i in range(1, len(arr)):
            tail.next = Node(arr[i])
            tail = tail.next

        ob = Solution()
        result = ob.alternatingSplitList(head)
        printList(result[0])
        printList(result[1])

# } Driver Code Ends