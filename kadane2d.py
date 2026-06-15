rows=int(input("enter the rows:"))
cols=int(input("Enter the cols:"))
matrix=[]
for i in range(rows):
    row=[]
    values=input().split()
    for j in range(cols):
        row.append(values[j])
    matrix.append(row)
max_sum = float('-inf')
for r1 in range(rows):
    for c1 in range(cols):
        for r2 in range(r1, rows):
            for c2 in range(c1, cols):
                current_sum = sum(
                    matrix[i][j]
                    for i in range(r1, r2 + 1)
                    for j in range(c1, c2 + 1)
                )
                if current_sum > max_sum:
                    max_sum = current_sum

print("Maximum Sum Submatrix =", max_sum)
