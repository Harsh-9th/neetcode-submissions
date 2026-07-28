# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if not head:
            return

        prev = None

        dele = head

        finder = head

        for _ in range(n - 1):
            if finder.next is None:
                return head
            finder = finder.next

        while finder.next:
            prev = dele
            dele = dele.next

            finder = finder.next

        if dele == head:
            head = dele.next
        
        else:
            prev.next = dele.next



        return head

        