#valid parantheses
class Ri():
    def ri(self,s:str)->bool:
        stack=[]
        di={')':'(','}':'{',']':'['}
        for i in s:
            if i in di:
                if stack and stack[-1]==di[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False

        #anather
        stack=[]
        for i in s:
            if i in '({[': # (i=='[') or (i=='{') or (i=='('):
                stack.append(i)
            else:
                if (not stack) or (((stack[-1]=='(') and (i !=')')) or ((stack[-1]=='{') and (i !='}')) or ((stack[-1]=='[') and (i !=']'))):
                    return False
                stack.pop()
        return True if not stack else False

        #anather
        while ('[]' in s) or ('{}' in s) or ('()' in s):
           s= s.replace('()','').replace('{}','').replace('[]','')
        return False if  len(s)!=0 else True
                     
riki = Ri()
print(riki.ri('(){}['))