class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None

    
    def get(self, index: int) -> int:
        if not self.head:   return -1
        current = self.head

        for _ in range(index):
            if current is None:
                return -1
            current = current.next
        if current is None:
            return -1
        return current.val

    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        self.head = new_node

        new_node.next = current
        return

    def insertTail(self, val: int) -> None:
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return
        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node
        return



    def remove(self, index: int) -> bool:
        if not self.head or index < 0:   return False

        if index == 0:
            self.head = self.head.next
            return True

        current = self.head
        for _ in range(index - 1):
            if current.next is None:
                return False

            current = current.next
        if current.next is None:
            return False

        current.next = current.next.next
        return True

        

        

    def getValues(self) -> List[int]:
        if not self.head:
            return []
        arr = []
        current = self.head

        while True:
            arr.append(current.val)
            current = current.next
            if current is None:
                break

        return arr
        
        
