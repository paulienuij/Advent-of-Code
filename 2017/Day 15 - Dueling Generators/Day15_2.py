factor_A = 16807
factor_B = 48271

A = 883
B = 879


total_judge = 0

def generate(last_val, fact, mult):
    r = 2147483647
    val = (last_val * fact) % r
    if val%mult == 0:
        return val
    else:
        return generate(val, fact, mult)

def binary_dig(i):
    return bin(i)[2:].zfill(16)[-16:]

for i in range(5000000):
    A = generate(A, factor_A, 4)
    B = generate(B, factor_B, 8)
    if binary_dig(A) == binary_dig(B):
        total_judge += 1
    if i% 50000 == 0:
        print('step ', int(i/50000))
print(total_judge)