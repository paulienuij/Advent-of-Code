def group(x):
    linked_to_x = [x]
    length_changes = 0
    last_len = 1
    global links

    while length_changes < 10:
        for link_ in links:
            l = link_[0]
            if l in linked_to_x:
                linked_to_x += link_[1]
                links.remove(link_)

        linked_to_x = list(set(linked_to_x))
        if len(linked_to_x) == last_len:
            length_changes += 1
        else:
            last_len = len(linked_to_x)

    return len(linked_to_x)

links = []

file = open(r"data.txt", "r", encoding="utf-8-sig")
lines = file.readlines()

for line in lines:
    link = int(line.split(' <-> ')[0])
    linked = [int(_) for _ in line.split(' <-> ')[1].split(',')]
    links.append([link, linked])

nb_groups = 0


while len(links) > 0:
      l = group(links[0][0])
      if l > 0:
          nb_groups += 1

print(nb_groups)



