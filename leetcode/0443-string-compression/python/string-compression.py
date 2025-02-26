# not in place
def a_compress(chars):
    l = 0
    r = 1
    result = ""
    while l <= len(chars) - 1:
        result += chars[l]
        group_length = 1
        while r <= len(chars) - 1 and chars[r] == chars[l]:
            group_length += 1
            r += 1
        if group_length > 1:
            result += str(group_length)
        l = r
        r += 1
    print("result: ", result)
    return len(result)

def compress(chars):
    i = 0
    ins = 0
    while i < len(chars):
        group_length = 1
        while (i + group_length < len(chars) and chars[i + group_length] == chars[i]):
            group_length += 1
        chars[ins] = chars[i]
        ins += 1
        if group_length > 1:
            # gotta split two-digit values into separate elements
            str_repr = str(group_length)
            chars[ins:ins + len(str_repr)] = list(str_repr)
            ins += len(str_repr)
        i += group_length
    print("chars: ", chars)
    return ins

print(compress(['a', 'a', 'b', 'b', 'c', 'c', 'c']), 6)
print(compress(['a']), 1)
print(compress(['a', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']), 4)

