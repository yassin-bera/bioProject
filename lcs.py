def lcs_three_strings(X, Y, Z):
    m, n, o = len(X), len(Y), len(Z)
    dp = {}

    for i in range(m + 1):
        for j in range(n + 1):
            for k in range(o + 1):
                if i == 0 or j == 0 or k == 0:
                    dp[(i, j, k)] = 0
                elif X[i - 1] == Y[j - 1] == Z[k - 1]:
                    dp[(i, j, k)] = dp[(i - 1, j - 1, k - 1)] + 1
                else:
                    dp[(i, j, k)] = max(dp[(i - 1, j, k)], dp[(i, j - 1, k)], dp[(i, j, k - 1)])


    lcs_str = []
    i, j, k = m, n, o
    while i > 0 and j > 0 and k > 0:
        if X[i - 1] == Y[j - 1] == Z[k - 1]:
            lcs_str.append(X[i - 1])
            i -= 1
            j -= 1
            k -= 1
        elif dp[(i - 1, j, k)] == dp[(i, j, k)]:
            i -= 1
        elif dp[(i, j - 1, k)] == dp[(i, j, k)]:
            j -= 1
        else:
            k -= 1

    return dp[(m, n, o)], ''.join(reversed(lcs_str))

X = input("Enter first string: ")
Y = input("Enter second string: ")
Z = input("Enter third string: ")

length, lcs_str = lcs_three_strings(X, Y, Z)
print(f"The length of the largest common subsequence is: {length}")
print(f"The largest common subsequence is: '{lcs_str}'")