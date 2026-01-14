def longestCommonPrefix(strs):
    if not strs:
        return ""

    first = strs[0]

    for i in range(len(first)):
        char = first[i]

        for word in strs:
            if i >= len(word) or word[i] != char:
                return first[:i]

    return first


# -------- Taking input from user --------
n = int(input("Enter number of words: "))
strs = []

for i in range(n):
    word = input(f"Enter word {i+1}: ")
    strs.append(word)

result = longestCommonPrefix(strs)
print("Longest Common Prefix:", result)
