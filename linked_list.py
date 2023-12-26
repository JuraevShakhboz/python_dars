class Node:
    def __init__(self, data):
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

    def delete(self, key_data):
        temp = self.head
        while temp:
            if temp.data == key_data:
                break
            prev = temp
            temp = temp.next

        if temp == None:
            print("No data found")
            return
        
        prev.next = temp.next
        temp.next = None
    
List = LinkedList()
List.head = Node("Dushanba")
List.head.next = Node("Seshanba")
List.head.next.next = Node("Chorshanba")
List.head.next.next.next = Node("Payshanba")

# print(List.head.next.next.data)
List.push("Foundation-24")
List.InsertInto(List.head.next.next, 'poliz')
List.append("karam")
List.append("olma")
List.append("tarvuz")
List.delete('olma')
List.delete('malina')
List.delete('karam')
List.printList()