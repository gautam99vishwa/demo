def find_placement(L, W, room, H):
    for i in range(L):
        row = room[i]
        
        # Check if the current row has enough space for the new pot
        if row[0] >= H:
            return (i, 0)
        
        # Find the position to insert the new pot in the current row
        for j in range(1, W):
            if row[j] >= H and row[j - 1] < H:
                return (i, j)
    
    # If no suitable spot is found, place the new pot in the last row and last column
    return None

# Input
L = int(input("Enter the number of rows (L): "))
W = int(input("Enter the number of columns (W): "))

room = []
for i in range(L):
    row = list(map(int, input(f"Enter the heights for row {i + 1} separated by spaces: ").split()))
    room.append(row)

H = int(input("Enter the height of the flower pot (H): "))

# Find the placement
placement = find_placement(L, W, room, H)

if placement is not None:
    print(placement[0], placement[1])
else:
    print("No suitable spot found to place the flower pot.")
