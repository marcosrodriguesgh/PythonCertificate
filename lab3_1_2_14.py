blocks = int(input("Enter the number of blocks: "))

height = last_level_blocks = current_level_blocks = 0

while blocks >= 0:
    if current_level_blocks <= last_level_blocks:
        blocks -= 1
        current_level_blocks += 1
    else:
        height += 1
        last_level_blocks = current_level_blocks
        current_level_blocks = 0

print("The height of the pyramid:", height)
