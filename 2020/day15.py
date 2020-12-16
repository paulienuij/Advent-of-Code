from collections import defaultdict

spoken = [6,4,12,1,20,0,16]

def play_game(spoken, n):
    for i in range(len(spoken), n+1):
        curr = spoken[-1]

        if curr not in spoken[:-1]:
            spoken.append(0)
        else:
            reversedspoken = spoken[:-1][::-1]  # remove last item and then reverse list
            prev = reversedspoken.index(curr)  # get index of first occurrence of curr number in reversed list
            spoken.append(prev+1)
    return curr

print(play_game(spoken, 2020 ))
print(play_game(spoken, 30000000))