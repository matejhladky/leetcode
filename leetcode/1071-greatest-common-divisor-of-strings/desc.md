## notes
- the second solution is more advanced/mathematical

## solutions
### 1. brute-force
- main idea: try all prefixes (base)
- order: start with the entire shorter string and keep removing letters
- check:
    - check is the length of str is divisible by base
    - multiply base by the number of times the the legnths divide and check if it's equal to str
- time: O(min(m, n) * (m + n))
    - m and n are the lengths of str1 and str2
    - we check every prefix string base of the shorter string and verify if both strings are made by multiples of base
    -> there are up to min(m, n) bases
    -> each check involves iterating over the two strings, which costs O(m + n)
- space: O(min(m, n)) - we need to keep a copy of base in each iteration

### 2. GCD
1. how to verify if there's ANY divisible string?
    - suppose there's a string base, so that str1 and str2 are multiples of base
    - thus, their concatenation must be consistent regardless of the order (str1 + str2 = str2 + str1), if they contain multiples of the same base
    -> we need to check if the concatenations are the same for both orders - if so, there exists a GCD string
2. if there are, what is the length of the GCD string
    - take the GCD of the lengths of both strings - that will be used by gcdBase (e.g. len(str1) = 9 and len(str2) = 6 --> gcdBase = ABC)
    - GCD string cannot be shorter than gcdBase - proof by contradiction:
        - assume len(shorterBase) < len(gcdBase)
        - len(shorterBase) is a divisor of len1 and len2
        - since len(gcdBase) is the GCD of len1 and len2, len(gcdBase) is divisible by len(shorterBase)
        - str1 and str2 contain multiples of gcdBase, so gcdBase is also divisible string, so GCD string is at least as long as gcdBase
        -> thus, it's not possible for the GCD string to be shorter than gcdBase
    - GCD string cannot be longer than gcdBase:
        - assume len(longerBase) > len(gcdBase)
        - this contradicts that len(gcdBase) is the GCD of len1 and len2
    => in conclusion, if there exists a divisible string, GCD string must be gcdBase
- algorithm:
    1. check if the concatenations of str1 and str2 are the same in both orders
    2. get the gcdLength of str1 and st2
    3. return the prefix string of gcdLength of either str1 or str2
- complexity:
    - time: O(m + n)
        - need to compare two concatenations of length O(m + n), which takes O(m + n) time
        - Euclidian algorithm for GCD takes log(m * n) tim
        - overall complexity if O(m + n)
    - space: O(m + n) - need to compare/store the two concatenations