class Solution(object):
    def isValid(self, s):
        correspondances = {')': '(', ']': '[', '}': '{'}
        pile = []
        
        for c in s:
            if c in correspondances.values():
                pile.append(c)
            elif c in correspondances:
                if not pile or pile.pop() != correspondances[c]:
                    return False
        
        return not pile





        