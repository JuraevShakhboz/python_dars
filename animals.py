animals = ["dog", "cat", "bat", "cock", "cow", "pig",
           "fox", "ant", "bird", "lion", "wolf", "deer", "bear",
           "frog", "hen", "mole", "duck", "goat"]

def count_animals(st):
    counts = []
    x = 0
    for animal in animals:
        txt = ""
        for i in animal:
            if i in st:
                txt += i
        if txt == animal:
            x += 1
            if txt not in counts:
                counts.append(txt)

    return f"count_animals(st)-> {x} {counts}"

st = input()
print(count_animals(st))