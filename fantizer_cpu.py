inv = {
    "arrow": 16,
    "life": 3,
    "poison": 1,
    "dragon": 9,
    "loons": 12,
}


def inventory(dic):
    total = 0
    for d, i in dic.items():
        total += i
        print(i, d)
    print(f"Total number of items in inventory were : {total}")


# CPU Driver Code
inventory(inv)
