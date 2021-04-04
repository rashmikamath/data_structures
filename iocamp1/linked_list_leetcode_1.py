class Solution:
    def partition(self, head, x):
        
        beforeHead = Node(0)
        before = beforeHead
        afterHead = Node(0)
        after = afterHead
        while(head):
            if head.data >= x:
                after.next = head
                after = after.next
            else:
                before.next = head
                before = before.next
            head = head.next
        
        
        after.next = None        
        before.next = afterHead.next
        
        return beforeHead.next

class Node:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_next(self):
        return self.next

    def set_next(self, node):
        self.next = node

class LinkedList():
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
    
    def get_head(self):
        return self.head

    def set_head(self, head):
        self.head = head


    def get_tail(self):
        return self.tail

    def set_tail(self, tail):
        self.tail = tail

    def append(self, append_value):
        if self.head is None:
            self.head = append_value
        else:
            self.tail = self.tail.set_next(append_value)
        self.tail = append_value

    def print_link_list(self):
        print_val = self.head
        while print_val is not None:
            print(print_val.data)
            print_val = print_val.next

    def delete_node(self, toDelete, prev):
        if toDelete is None:
            return
        if toDelete == self.head:
            self.head = toDelete.next
        if toDelete == self.tail:
            self.tail = prev
        if prev is not None:
            prev.next = toDelete.next

    def delete_node_noprev(self, toDelete):
        next = toDelete.get_next()
        if next == None:
            return 
        toDelete.set_data(next.get_data())
        self.delete_node(next, toDelete)

    def delete_nth_node(self, n):
        temp = self.head
        count = 0
        while temp is not None:
            count += 1
            if count == n:
                self.delete_node_noprev(temp)
            temp = temp.next

node1 = Node(1)
node2 = Node(4)
node3 = Node(3)
node4 = Node(2)
node5 = Node(5)
node6 = Node(2)
node7 = Node(700)
list_data = LinkedList()
list_data.head = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = None 
#node6.next = node7

s = Solution()
l = s.partition(node1, 3)
import pdb
pdb.set_trace()