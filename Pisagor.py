def pisagor_bulma():
    pisagorlar = list()

    for a in range(1, 101):
        for b in range(1, 101):
            c = (a ** 2 + b ** 2) ** 0.5
            if (c == int(c)):
                pisagorlar.append((a, b, int(c)))
    return pisagorlar

for i in pisagor_bulma():
    print(i)