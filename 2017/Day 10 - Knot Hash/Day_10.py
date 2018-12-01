def knot_hash(string_, lengths_):
    current_pos = 0
    skip = 0

    for l in lengths_:
        to_be_rev = []

        # create a list containg the part to be reversed
        for i in range(current_pos, current_pos + l):
            to_be_rev.append(string_[i % str_len])
            # print('to be rev:', to_be_rev)

        # replace the chunk of the string by the reversed part
        for i in range(current_pos, current_pos + l):
            string_[i % str_len] = to_be_rev[-(i - current_pos) - 1]
            # print(string_[i%str_len])

        current_pos = current_pos + skip + l
        skip += 1

    return string_[0] * string_[1]

lengths = [230, 1, 2, 221, 97, 252, 168, 169, 57, 99, 0, 254, 181, 255, 235, 167]
#lenghts = [3,4,1,5]

string = []
str_len = 256
#str_len = 5

for i in range(0, str_len):
    string.append(i)

print(knot_hash(string, lengths))

