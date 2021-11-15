inv = dict()
names = []
manys = []


def inventory(dic):
    total = 0
    for d, i in dic.items():
        total += i
        print(i, d)
    print(f"Total number of items in inventory were : {total}")


print("Welcome to Fantizer")
n = int(input("How many itemes yo got ? "))
inv_cp = {}
for n in range(n):
    name = str(input("Yo item got any name : "))
    names.append(name)
    many = int(input("How much yo got in that name : "))
    manys.append(many)

# print(names)
# print(manys)

# BUGG
# for x, y in names, manys:
#     hand = dict(x=y)

# Player One Driver Code
# inventory(hand)
