with open("day1/input.txt", "r") as file:
    data = file.read().splitlines()
print(data)

lock_nums = list(range(0,100))
hit_zero = 0
start = 50

for line in data:
    
    if line[0] == "L":
        full_cycles = int(line[1:]) // 100
        hit_zero += full_cycles
        
        remaining_movement = int(line[1:]) % 100
        if remaining_movement >= start and start != 0:
            hit_zero += 1
            
        start = (start - int(line[1:])) % 100
        
    elif line[0] == "R":
        full_cycles = int(line[1:]) // 100
        hit_zero += full_cycles
        
        remaining_movement = int(line[1:]) % 100
        if start + remaining_movement >= 100:
            hit_zero += 1
            
        start = (start + int(line[1:])) % 100
print(hit_zero)