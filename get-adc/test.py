cmp = int(input())

def comp(input, comp):
    return comp < input


s = bin(0)[2:].zfill(8)

print(s[:1])

for x in range(0, 8):
    j = s[:x] + '1' + s[(x+1):]
    if comp(int(j, 2), cmp):
        s = s[:x] + '0' + s[(x+1):]
    else:
        s = s[:x] + '1' + s[(x+1):]
    print(s)