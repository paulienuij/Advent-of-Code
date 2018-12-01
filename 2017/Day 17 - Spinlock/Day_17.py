stepsize = 355

buffer = [0]
cur_pos = 0

for i in range(1,2018):
    l = len(buffer)
    cur_pos = (cur_pos+stepsize)%l+1
    buffer.insert(cur_pos, i )

i = buffer.index(2017)
print('the value after 2017 is :', buffer[i+1])


