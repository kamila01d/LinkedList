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

    def findDuplicates(self):
        current = self.head
        while current is not None:
            tmp = current
            while tmp.next is not None:
                if tmp.next.value == current.value:
                    tmp.next = tmp.next.next
                else:
                    tmp = tmp.next
            current = current.next
    def ifPalindrome(self):

        current = self.head
        palList = []

        while current is not None:
            palList.insert(0,current.value)
            current = current.next

        tmp = self.head
        while tmp is not None:
            if tmp.value != palList[0]:
                print("not palindrome")
                return
            else:
                del palList[0]
                tmp = tmp.next

        print("palindrome")
    def isPal(self):
        slow = self.head
        fast = self.head

        stack = []

        while fast != None and fast.next != None:
            stack.insert(0,slow.value)
            slow = slow.next
            fast = fast.next.next

        if fast != None:
            slow = slow.next

        while(slow!=None):

            top = stack[0]
            del stack[0]

            if top != slow.value:
                print("Not palindrome")
                return
            slow = slow.next
        print("palindrome")








    def print(self):
        current = self.head
        while current is not None:
            print(current.value, end=" ")
            current = current.next
        print("")

l = LinkedList()
l.push_back(5)
l.push_back(7)
l.push_back(4)
l.push_back(8)
l.push_back(4)
l.push_back(7)
l.push_back(3)
l.print()
l.print()
l.ifPalindrome()
l.isPal()











