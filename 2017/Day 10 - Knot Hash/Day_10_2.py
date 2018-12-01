def knot_hash (string, lengths):
    str_len = len(string)
    global current_pos
    global skip
    for l in lengths:
        to_be_rev = []
        # create a list containing the part to be reversed
        for i in range(current_pos, current_pos + l):
            to_be_rev.append(string[i % str_len])
        # replace the chunk of the string by the reversed part
        for i in range(current_pos, current_pos + l):
            string[i % str_len] = to_be_rev[-(i - current_pos) - 1]
        current_pos = current_pos + skip + l
        skip += 1
    return string

current_pos = 0
skip = 0

lengths = [ord(x) for x in '230,1,2,221,97,252,168,169,57,99,0,254,181,255,235,167']
lengths += [17, 31, 73, 47, 23]

string = []
for i in range(256):
    string.append(i)

for i in range(64):
    string = knot_hash(string, lengths)

sparse_hash = string
dense_hash = []

for i in range(0,256,16):
    xor_16 = sparse_hash[i] ^ sparse_hash[i+1]
    for j in range(2, 16):
        xor_16 ^= sparse_hash[i+j]
    dense_hash.append(hex(xor_16)[2:].zfill(2))
    #print(hex(xor_16)[2:].zfill(2))

hash = ""
for i in dense_hash:
    hash += str(i)

print(hash)
