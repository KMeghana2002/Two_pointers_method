def reverse_str(s):
    left=0
    right=len(s)-1
    while left<right:
        s[left],s[right]=s[right],s[left]
        left=left+1
        right=right-1
        return s
s=['h','e','l','l','o']
result=reverse_str(s)
print(result)
