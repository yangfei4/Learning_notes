# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Add two numbers
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        cur = ListNode()
        result = cur.next
        addReminder = 0

        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            sum = x+y+addReminder
            cur.next = ListNode(val = sum%10)

            addReminder = (sum)//10

            if l1 : l1 = l1.next
            if l2 : l2 = l2.next
            cur = cur.next
        
        if addReminder:
            cur.next = ListNode(val=addReminder)

        return result.next



class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        save = []
        count = 0

        if len(s) == 1 : return 1
        
        for x in s:
            if x in save:
                if len(save)>count:
                    count = len(save)
                idx = save.index(x)+1
                for _ in range(idx):
                    save.pop(0)
            save.append(x)

        if len(s)==len(save) or len(save)>count: return len(save)
        return count

class Solution(object):
    # Slide Windows
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        save = []
        cur_len = 0
        max_len = 0

        for x in s:
            cur_len += 1
            while x in save:
                cur_len -= 1
                save.pop(0)
            if cur_len > max_len: max_len = cur_len

            save.append(x)

        return max_len

s = "a"
# test = Solution()
# print(test.lengthOfLongestSubstring(s))

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s_len = len(s)
        t_len = len(t)
        if t_len>s_len: return ""

        Done = False
        left = 0
        right = left+t_len
        curr = s_len[left:right]

        while not Done:
            pass
