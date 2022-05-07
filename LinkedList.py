class Node:
    def __init__(self,value=None,next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def sizeL(self):
        return '{}'.format(self.size)

    def push_front(self,value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
            self.size +=1
            return None
        else:
            temp = self.head
            self.head = Node(value,temp)
            self.size += 1

    def push_back(self,value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
            self.size +=1
            return None
        else:
            newTail = Node(value,None)
            self.tail.next = newTail
            self.tail = newTail
            self.size += 1
            return None

    def pop_front(self):
        if self.head is None:
            print("Linked list is already empty !!!")
        elif self.head is self.tail:
            self.head = None
            self.tail = None
            self.size -= 1

        else:
            self.head = self.head.next
            self.size -= 1

    def pop_back(self):
        if self.tail is None:
            print("Linked list is already empty !!!")
            return None
        elif self.head is self.tail:
            self.head = None
            self.tail = None
            self.size -= 1
            return None

        else:
            current = self.head
            prev = None

            while current.next is not None:
                prev = current
                current = current.next

            self.tail = prev
            prev.next = None


    def print(self):
        current = self.head
        while current is not None:
            print(current.value, end=" ")
            current = current.next
        print("")









