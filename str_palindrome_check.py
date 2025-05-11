def str_palindrome(s):
    left=0
    right=len(s)-1
    while left<right:
        if s[left]==s[right]:
            left=left+1
            right=right-1
            return True
        return False
s="madam"
result=str_palindrome(s)
print(result)
