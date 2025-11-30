class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        temp=''         #a,b,c,d
        for i in path:
            if i=='/':
                if temp=='..' and stack:
                    stack.pop()
                elif temp and (temp!='.' and temp!='..'): 
                    stack.append(temp)
                temp=''
            else:
                temp+=i
        if temp=='..' and stack:
            stack.pop()
        elif temp and (temp!='.' and temp!='..'): 
            stack.append(temp)
        path=''
        stack2=[]
        while stack:
            stack2.append('/'+stack.pop())
        while stack2:
            path+=stack2.pop()
        return path or '/'
            
#home,foo

