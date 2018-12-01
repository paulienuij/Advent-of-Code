factor_A = 16807
factor_B = 48271

A = 883
B = 879


total_judge = 0

def generate(last_val, fact):
    r = 2147483647
    return (last_val * fact) % r

def binary_dig(i):
    return bin(i)[2:].zfill(16)[-16:]

for i in range(40000000):
    A = generate(A, factor_A)
    B = generate(B, factor_B)
    if binary_dig(A) == binary_dig(B):
        total_judge += 1
    if i% 400000 == 0:
        print('step ', int(i/400000)):
print(total_judge)
