import sys
st = list()
q=list()
class Solution:
    def pushCharacter(self, s):
        global st
        st.append(s)
    def enqueueCharacter(self, s):
        global q
        q.insert(0,s)   
    def popCharacter(self):
        global st
        return(st.pop())
    def dequeueCharacter(self):
        global q
        return(q.pop()) 
s=input()
#Create the Solution class object
obj=Solution()   

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")    