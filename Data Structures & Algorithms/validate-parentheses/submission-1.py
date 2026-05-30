class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        bracks = {")":"(", "]":"[", "}":"{"}
        for data in s:
            if data in bracks:
                top = stack.pop() if stack else "#"

                if bracks[data] != top:
                    return False
            else:
                stack.append(data)

        return not stack
        
            


        