from typing import Optional, List


# class Solution:
#
#     def add_two_numbers(self, l1: Optional[List], l2: Optional[List]):
#         j = 0
#         k = 0
#         stack = []
#         for i in reversed(range(len(l1))):
#             try:
#                 if l1[k] + l2[k] > 9:
#                     stack.append((l1[k] + l2[k]) % 10 + j)
#                     j = (l1[i] + l2[k]) // 10
#                 else:
#                     stack.append(l1[k] + l2[k] + j)
#                     j = 0
#                 k += 1
#             except IndexError:
#                 stack.append((l1[k] + j) % 10)
#                 k += 1
#                 if k == len(l1):
#                     stack.append((l1[k - 1] + j) // 10)
#         return stack
#
#
# print(Solution().add_two_numbers([9,9,9,9,9,9,9], [9,9,9,9]))


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    @staticmethod
    def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # dummy = ListNode()
        # cur = dummy
        # carry = 0
        # while l1 or l2 or carry:
        #     v1 = l1.val if l1 else 0
        #     v2 = l2.val if l2 else 0
        #
        #     val = v1 + v2 + carry
        #     carry = val // 10
        #     val = val % 10
        #     cur.next = ListNode(val)
        #
        #     cur = cur.next
        #     l1 = l1.next if l1 else None
        #     l2 = l2.next if l2 else None
        # return dummy.next

        dummy = ListNode()
        current = dummy
        carry = 0

        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            s = carry + x + y
            carry = s // 10
            current.next = ListNode(s % 10)
            current = current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry > 0:
            current.next = ListNode(carry)

        return dummy.next
