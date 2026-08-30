class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            #print(i, stack)
            if i in {'+', '-', '*', '/'}:
                if len(stack) >= 2:
                    arg2 = stack.pop()
                    arg1 = stack.pop()
                    stack.append(self.op(i, arg1, arg2))
            else:
                z = int(i)
                stack.append(z)
        #print(stack)
        return int(stack[-1])

    def op(self, op: str, arg1: str, arg2: str):
        l = int(arg1)
        r = int(arg2)
        #print(op, l, r)
        if op == '+': return l+r
        elif op == '-': return l-r
        elif op == '*': return l*r
        elif op == '/': return l/r
 