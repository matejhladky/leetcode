def reverseVowels(s):
    s = list(s)
    i = 0
    j = len(s) - 1
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'} # better to use set for O(1)
    while i < j:
        if s[i] not in vowels:
            i += 1
            continue

        if s[j] not in vowels:
            j -= 1
            continue

        s[i], s[j] = s[j], s[i]

        i += 1
        j -= 1

    return "".join(s)

# cool kids approach
def reverseVowels(s):
    vowels=[i for i in s if i in "aeiouAEIOU"]
    result=[i if i not in "aeiouAEIOU" else vowels.pop() for i in s]
    return "".join(result)



print(reverseVowels('IceCreAm'), "AceCreIm")
print(reverseVowels('leetcode'), "leotcede")