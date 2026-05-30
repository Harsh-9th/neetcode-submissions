class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        bracks = {")":"(", "]":"[", "}":"{"}
        for data in s:
            if data not in bracks:
                stack.append(data)
            elif stack and bracks[data] == stack[-1]:
                    stack.pop()
            else:
                return False

        return not stack
        
            


        