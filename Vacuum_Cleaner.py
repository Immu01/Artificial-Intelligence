def vacuum_cleaner_agent(room, start):
    x, y = start
    steps = 0
    print("Initial Room State:")
    for row in room:
        print(row)
    print()
    
    while True:
        if room[x][y] == 'D':
            room[x][y] = 'C'
            print(f"Cleaned dirt at ({x}, {y})")
            steps += 1
        
        if all(cell == 'C' for row in room for cell in row):
            print("All rooms are clean!")
            break
        
        if y + 1 < len(room[0]) and room[x][y + 1] == 'D':
            y += 1
        elif x + 1 < len(room) and room[x + 1][y] == 'D':
            x += 1
        elif y - 1 >= 0 and room[x][y - 1] == 'D':
            y -= 1
        elif x - 1 >= 0 and room[x - 1][y] == 'D':
            x -= 1
        else:
            y = (y + 1) % len(room[0])
            if y == 0:
                x = (x + 1) % len(room)
                
        steps += 1

    print("\nFinal Room State:")
    for row in room:
        print(row)
    print(f"\nTotal Steps Taken: {steps}")

room = [['D', 'C', 'D'], ['C', 'D', 'C'], ['D', 'C', 'C']]
start_position = (0, 0)
vacuum_cleaner_agent(room, start_position)


#Output:

# Initial Room State:
# ['D', 'C', 'D']
# ['C', 'D', 'C']
# ['D', 'C', 'C']

# Cleaned dirt at (0, 0)
# Cleaned dirt at (0, 2)
# Cleaned dirt at (1, 1)
# Cleaned dirt at (2, 0)
# All rooms are clean!

# Final Room State:
# ['C', 'C', 'C']
# ['C', 'C', 'C']
# ['C', 'C', 'C']

# Total Steps Taken: 10