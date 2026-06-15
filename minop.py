s = input("Enter first string: ")
t = input("Enter second string: ")

m = len(s)
n = len(t)

dp = []

for i in range(m + 1):
    row = []
    for j in range(n + 1):
        row.append(0)
    dp.append(row)

for i in range(m + 1):
    dp[i][0] = i

for j in range(n + 1):
    dp[0][j] = j

for i in range(1, m + 1):
    for j in range(1, n + 1):

        if s[i - 1] == t[j - 1]:
            dp[i][j] = dp[i - 1][j - 1]

        else:
            insert = dp[i][j - 1]
            delete = dp[i - 1][j]
            replace = dp[i - 1][j - 1]

            dp[i][j] = 1 + min(insert, delete, replace)

print("Minimum operations =", dp[m][n]
