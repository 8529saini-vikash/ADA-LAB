def longestCommonSubsequence(text1, text2):
    rows = len(text1) + 1
    cols = len(text2) + 1
    dp = [[0] * cols for _ in range(rows)]

    for i in range(1, rows):
        for j in range(1, cols):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[-1][-1]


def minDistance(word1, word2):
    rows = len(word1) + 1
    cols = len(word2) + 1
    dp = [[0] * cols for _ in range(rows)]

    for i in range(rows):
        dp[i][0] = i
    for j in range(cols):
        dp[0][j] = j

    for i in range(1, rows):
        for j in range(1, cols):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],       # Deletion
                    dp[i][j - 1],       # Insertion
                    dp[i - 1][j - 1]    # Replacement
                )

    return dp[-1][-1]


# Example input
text1 = "ABCBDAB"
text2 = "BDCABA"
word1 = "horse"
word2 = "ros"

print("Longest Common Subsequence")
print("String 1:", text1)
print("String 2:", text2)
print("LCS Length:", longestCommonSubsequence(text1, text2))

print("\nMinimum Edit Distance")
print("Word 1:", word1)
print("Word 2:", word2)
print("Minimum Operations:", minDistance(word1, word2))
