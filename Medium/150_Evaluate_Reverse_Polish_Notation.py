class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        op = {"+":(lambda x, y: x + y), "-":(lambda x, y: y-x), "*": (lambda x, y: x * y), "/": (lambda x, y: y / x if (x*y >= 0) else -(abs(y)/abs(x)))}
        # use stack 
        stackOperands = [] 
        for tok in tokens: 
            if tok not in op:
                stackOperands.append(int(tok))
            else: 
                stackOperands.append(op[tok](stackOperands.pop(), stackOperands.pop()))
        return stackOperands.pop()
