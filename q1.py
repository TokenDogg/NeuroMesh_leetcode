def subsequence_string(source, target):
    count = 0
    s_pointer = 0
    t_pointer = 0
    s_len = len(source)

    while t_pointer < len(target):
        if s_pointer == s_len:
            if t_pointer == 0 or target[count] == target[t_pointer]:
                return -1
            s_pointer = 0
            count += 1
        if source[s_pointer] == target[t_pointer]:
            t_pointer += 1

        s_pointer += 1

    return count + 1

print(subsequence_string("abc","abcbc"))
print(subsequence_string("xyz","xzyxz"))
print(subsequence_string("abc","acdbc"))
