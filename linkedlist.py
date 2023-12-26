class Node:
    def __init__(self,data):
        self.data = data
        self.next = None



class LinkedList:
    def __init__(self):
        self.head = None

    
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
    
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def InsertInto(self, pre_node, data):
        new_node = Node(data)
        new_node.next = pre_node.next
        pre_node.next = new_node
    
    def append(self, data):
        new_node = Node(data)
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def getMax(self):
        temp = self.head
        self.max = self.head.data
        while temp:
            if self.max < temp.data:
                self.max = temp.data
            temp=temp.next
        print(self.max)

    def getMin(self):
        temp = self.head
        self.min = self.head.data
        while temp:
            if self.min > temp.data:
                self.min = temp.data
            temp = temp.next
        print(self.min)

    def inter_sum(self):
        sum = self.min + self.max
        print(sum)
        

lst = LinkedList()
lst.head = Node(13)
lst.head.next = Node(14)
lst.head.next.next = Node(14)
lst.head.next.next.next = Node(16)

lst.inter_sum()