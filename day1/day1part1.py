with open("day1/input.txt", "r") as file:
    data = file.read().splitlines()
print(data)

lock_nums = list(range(0,100))
hit_zero = 0
start = 50
for line in data:
    if line[0] == "L":
        x = (start - int(line[1:])) % 100
        start = lock_nums[x]
    elif line[0] == "R":
        y = (start + int(line[1:])) % 100
        start = lock_nums[y]
    if start == 0:
        hit_zero += 1
    print(start)

print(hit_zero)