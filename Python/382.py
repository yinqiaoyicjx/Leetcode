# Definition for singly-linked list.
import random
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.list=head



    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        choice=self.list.val
        head,i=self.list.next,1

        while head != None:

            i+=1
            k=random.random()
            if k <= 1.0/i:
                choice=head.val
            head=head.next

        return choice

