# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if not head:
            return

        dummy = ListNode(None)

        dummy.next = head

        dele = dummy

        finder = dummy

        for _ in range(n):
            if finder.next is None:
                return head
            finder = finder.next

        while finder.next:
            dele = dele.next

            finder = finder.next

        

        dele.next = dele.next.next

        head = dummy.next


        return head

        