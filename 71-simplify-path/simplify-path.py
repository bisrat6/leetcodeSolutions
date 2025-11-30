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
        return "/" + "/".join(stack)

            
#home,foo

