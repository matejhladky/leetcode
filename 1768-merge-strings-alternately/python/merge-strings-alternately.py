# two pointers
def mergeAtlernately(word1, word2):
    i = 0
    j = 0
    result = []
    while i < len(word1) and j < len(word2):
        result.append(word1[i])
        result.append(word2[i])
        i += 1
        j += 1
    result.append(word1[i:])
    result.append(word2[i:])

    return "".join(result)

# one pointer
def mergeAtlernately(word1, word2):
    n = max(len(word1), len(word2))
    result = []
    for i in range(n):
        if i < len(word1):
            result.append(word1[i])
        if i < len(word2):
            result.append(word2[i])

    return "".join(result)


print(mergeAtlernately("abcd", "pqr"))