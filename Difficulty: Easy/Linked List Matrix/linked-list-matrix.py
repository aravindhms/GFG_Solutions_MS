#User function Template for python3



class Node():
    def __init__(self,x):
        self.data = x
        self.right = None
        self.down=None



class Solution:
    def constructLinkedMatrix(self, mat):
        #your code goes here
        if not mat or not mat[0]:
            return None

        n = len(mat)
        head = None
        prev_row = [None] * n

        for i in range(n):
            row_head = None
            prev_node = None

            for j in range(n):
                new_node = Node(mat[i][j])

                if j == 0:  # First node in the row
                    row_head = new_node
                else:  # Link nodes horizontally
                    prev_node.right = new_node

                if i > 0:  # Link nodes vertically
                    prev_row[j].down = new_node

                prev_node = new_node
                prev_row[j] = new_node

            if i == 0:
                head = row_head  # Set the head of the linked list

        return head

#{ 
 # Driver Code Starts
class Node():

    def __init__(self, x):
        self.data = x
        self.right = None
        self.down = None


def display(head):
    Dp = head
    while Dp:
        Rp = Dp
        while Rp:
            print(Rp.data, end=" ")
            if Rp.right:
                print(Rp.right.data, end=" ")
            else:
                print("null", end=" ")
            if Rp.down:
                print(Rp.down.data, end=" ")
            else:
                print("null", end=" ")
            Rp = Rp.right
        Dp = Dp.down


if __name__ == "__main__":
    for _ in range(int(input())):
        # First row input
        a = list(map(int, input().strip().split()))
        n = len(a)

        # Input the matrix
        mat = [a]
        for i in range(1, n):
            row = list(map(int, input().strip().split()))
            mat.append(row)

        # Create a Solution object and construct the linked matrix
        obj = Solution()
        head = obj.constructLinkedMatrix(mat)
        if head is None:
            print(-1)
            continue
        display(head)
        print()

# } Driver Code Ends