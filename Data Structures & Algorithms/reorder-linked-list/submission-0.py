# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return

        slow = head

        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second_half = slow.next
        slow.next = None
        prev = None

        current = second_half
        while current:
            next_node = current.next
            current.next = prev
            prev = current

            current = next_node


        first_half = head
        second_half = prev

        while second_half:
            temp1 = first_half.next
            temp2 = second_half.next


            first_half.next = second_half

            second_half.next = temp1

            first_half = temp1
            second_half = temp2



        