def create_target_matrix(m, n, targets, columnIndices, rowPointers):
    matrix = [['z' for _ in range(n)] for _ in range(m)]

    for i in range(m):
        start_idx = rowPointers[i]
        end_idx = rowPointers[i + 1]

        for j in range(start_idx, end_idx):
            col = columnIndices[j]
            matrix[i][col] = targets[j]

    return matrix

# Input
n = int(input())
m = int(input())

targets = input().split()
columnIndices = list(map(int, input().split()))
rowPointers = list(map(int, input().split()))

ans = create_target_matrix(m, n, targets, columnIndices, rowPointers)

# Print the resulting matrix
for row in ans:
    print(" ".join(row))
