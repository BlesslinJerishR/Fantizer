inv = {}
names = []
manys = []


def inventory(dic):
    total = 0
    for d, i in dic.items():
        total += i
        print(i, d)
    print(f"Total number of items in inventory were : {total}")


print("Welcome to Fantizer")
n = int(input("How many items yo got ? "))

for n in range(n):
    name = str(input("Yo item got any name : "))
    names.append(name)
    many = int(input("How much yo got in that name : "))
    manys.append(many)

# fire @test
# print(names)
# print(manys)

# BUGG >> Fixed >> Closed
army = 0
for x in names:
    for y in manys:
        army += y
        inv[x] = y
        manys.remove(y)
        break
# print(str(inv))

# Player One Driver Code
print("Inventory : ")
inventory(inv)
print(f"Total army camp : {army}")

