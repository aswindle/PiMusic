def answer(s):
    # Worst-case: entire string is the pattern, meaning only 1 copy
    result = 1
    for i in range(1, len(s)+1):
        # If s isn't a multiple of i, there can't be i copies of a pattern
        if len(s)%i != 0:
            continue
        else:
            # pattern is the first 1/ith of s
            # if i copies of pattern equal s, then we've found a new highest number
            pattern = s[0:(len(s)//i)]
            if (pattern*i == s):
                result = i
    return result
            

print(answer("aaaaaa"))