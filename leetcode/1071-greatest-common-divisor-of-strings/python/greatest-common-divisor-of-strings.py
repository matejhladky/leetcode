# brute-force
def gcdOfStrings(str1, str2):
    len1 = len(str1)
    len2 = len(str2)

    def valid(k):
        if len1 % k or len2 % k:
            return False
        n1 = len1 // k
        n2 = len2 // k
        base = str1[:k]
        return str1 == n1 * base and str2 == n2 * base

    for i in range(min(len1, len2), 0, -1):
        if valid(i):
            return str1[:i]
    return ""


def gcdOfStrings(str1, str2):
    if str1 + str2 != str2 + str1:
        return ""
    
    def gcd(len1, len2):
        min_val = min(len1, len2)
        for i in range(min_val, 0, -1):
            if len1 % 1 == 0 and len2 % 1 == 0:
                return i
        return 1
    
    gcdLength = gcd(len(str1), len(str2))
    return str1[:gcdLength]

print(gcdOfStrings("ABCABC", "ABC"))
