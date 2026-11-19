# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        
        new_cur = merged_head = ListNode(0)

        cur_1 = list1
        cur_2 = list2
        
        while cur_1 and cur_2:
            if cur_1.val < cur_2.val:
                new_cur.next = cur_1
                cur_1 = cur_1.next
            else:
                new_cur.next = cur_2
                cur_2 = cur_2.next
            
            new_cur = new_cur.next
        
        if cur_1:
            new_cur.next = cur_1
        
        if cur_2:
            new_cur.next = cur_2
        
        return merged_head.next
            


