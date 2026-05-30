class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        bracks = {")":"(", "]":"[", "}":"{"}
        for data in s:
            if data in bracks:
                if stack and stack[-1] == bracks[data]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(data)

        return not stack
        
            


        