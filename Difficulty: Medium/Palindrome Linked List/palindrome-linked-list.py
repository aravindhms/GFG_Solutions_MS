#User function Template for python3
'''
	Your task is to check if given linkedlist
	is a pallindrome or not.
	
	Function Arguments: head (reference to head of the linked list)
	Return Type: boolean , no need to print just return True or False.
'''
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None


#Function to check whether the list is palindrome.
class Solution:
    def isPalindrome(self, head):
        #code here
        if not head or not head.next:
            return True

        # Find the middle of the linked list
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half of the list
        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node

        # Compare the first half and the reversed second half
        left, right = head, prev
        while right:
            if left.data != right.data:
                return False
            left = left.next
            right = right.next

        return True

#{ 
 # Driver Code Starts
#main


class Node:
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Utility function to prit the linked LinkedList
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            temp = temp.next
        print("")


if __name__ == '__main__':
    t = int(input())
    while (t > 0):
        llist = LinkedList()
        values = input().strip().split()
        for i in reversed(values):
            llist.push(i)
        flag = Solution().isPalindrome(llist.head)
        if flag:
            print("true")
        else:
            print("false")
        t -= 1
# Contributed by: Harshit Sidhwa

# } Driver Code Ends