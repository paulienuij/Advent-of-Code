stepsize = 355

buffer = [0]
cur_pos = 0

for i in range(1,50000000):
    l = len(buffer)
    cur_pos = (cur_pos+stepsize)%l+1
    buffer.insert(cur_pos, i )
    if i % 500000 == 0:
        print("progress: ", i/500000, '%')

i = buffer.index(0)
print('the value after 0 is :', buffer[i+1])


50000000
