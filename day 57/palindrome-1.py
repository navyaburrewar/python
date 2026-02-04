### check the palimdrome using the recursion

def palindrome(m):

    if len(m)<=1:
        return True
    if m[0]!=m[-1]:
        return False
    return palindrome(m[1:-1])

print(palindrome("madam")   ) 
print(palindrome("navya")   ) 
