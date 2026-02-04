## reversing a string  using recursion


def reverse(i):
    if len(i)==0:
        return i
    else:
        return reverse(i[1:])+i[0]
print(reverse("navya"))    




def num(m):
    if len(m)==0:
        return m
    else:
        return num(m[1:])+m[0]
print(num("123"))    