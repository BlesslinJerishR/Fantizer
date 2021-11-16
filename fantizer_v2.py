def add_inventory(inv, loot):
    for x, y in inv.items():
        for z in loot:
            inv[z] = y
            break
        return inv


def inventory(dic):
    total = 0
    for d, i in dic.items():
        total += i
        print(i, d)
    print(f"Total number of items in inventory were : {total}")


inv = {'gold': 42, 'haste': 3}
loot = ['gold', 'elixer', 'gems']

inn = add_inventory(inv, loot)
print(inn)
inventory(inn)
