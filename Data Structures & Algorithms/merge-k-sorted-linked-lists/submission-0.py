# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # n is length of largest list
        # k is number of lists
        # idea: reverse all lists first -- O(n * k)
        # then, find min among the lists -- O(k)
        # this happens n times?

        k = len(lists)

        # edge cases
        if k == 0:
            return None
        elif k == 1:
            return lists[0]


        def reverseList(lst: Optional[ListNode]) -> Optional[ListNode]:
            # standard linked-list reversing algorithm
            p, c = None, lst

            while c != None:
                n = c.next
                c.next = p
                p = c
                c = n
            
            return p



        # merging algorithm

        lst_a = lists[0]
        for i in range(1, k): # O(k) times
            tmp = None
            lst_b = lists[i]

            while lst_a != None and lst_b != None:
                a = lst_a.val
                b = lst_b.val

                if lst_a.val <= lst_b.val:
                    tmp = ListNode(lst_a.val, tmp)
                    lst_a = lst_a.next
                else:
                    tmp = ListNode(lst_b.val, tmp)
                    lst_b = lst_b.next

            # handle different-sized lists
            while lst_a != None:
                tmp = ListNode(lst_a.val, tmp)
                lst_a = lst_a.next
            
            while lst_b != None:
                tmp = ListNode(lst_b.val, tmp)
                lst_b = lst_b.next
            

            lst_a = reverseList(tmp) # O(n)

        return lst_a
        
        

