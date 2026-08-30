class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            print(c)
            matched = False
            if c == '}':
                if len(stack) == 0: return False
                if stack[-1] != '{': return False
                else: 
                    stack.pop()
                    matched = True
            if c == ']':
                if len(stack) == 0: return False
                if stack[-1] != '[': return False
                else: 
                    stack.pop()
                    matched = True
            if c == ')':
                if len(stack) == 0: return False
                if stack[-1] != '(': return False
                else: 
                    stack.pop()
                    matched = True

            if not matched: stack.append(c)

        return len(stack) == 0