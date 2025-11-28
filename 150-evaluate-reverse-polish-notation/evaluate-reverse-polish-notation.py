from typing import List
import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def operation(a:int,b:int,token:str)->int:
            match token:
                case '+':
                    return a+b
                case '-':
                    return a-b
                case '*':
                    return a*b
                case '/':
                    temp=a/b
                    return math.floor(temp) if temp>=0 else math.ceil(temp)

        stack=[]
        for i in tokens:
            try:
                stack.append(int(i))
            except:
                a=stack.pop()
                b=stack.pop()
                stack.append(operation(b,a,i))
        return stack.pop()


#0,17