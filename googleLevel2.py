# list of z values that have popped up in the past
seen = []

def answer(s, b):
    global seen
    # parse the numbers from the string
    x, y, z = get_xyz(s, b)
    # if z has shown up before, we've found a cycle
    if z in seen:
        return(len(seen)-seen.index(z))
    # if not, add it to the seen list and call answer on seen
    else:
        seen.append(z)
        return answer(z, b)

# parse the values of x, y, and z from the string
def get_xyz(s, b):
    k = len(s)
    digits = []
    for i in range(k):
        digits.append(int(s[i]))
    digits = sorted(digits)
    x = ""
    y = ""
    for i in range(k):
        y += str(digits[i])
        x += str(digits[-(i+1)])
    
    z = int(x, b) - int(y, b)
    z = dec_to_b(z, b, k)
    return x, y, z

# convert from base 10 to a string of length k in base b
def dec_to_b(num, b, k):
    retval = ""
    digits = []
    for x in range(k):
        digits.append(num%b)
        num = num//b
    digits.reverse()
    for x in range(0, k):
        retval += str(digits[x])
    return retval

print(answer("210022", 3))