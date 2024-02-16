#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#  implementation of the Levenshtein distance algorithm in python
# ---------------------------------------------------------------------------
#  the levenshtein_distance function takes two words as input and returns the Levenshtein distance between them. 
#  You can use this implementation to compute the edit distance between any pair of words.
#
##############################################################################

def levenshtein_distance(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i

    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

    return dp[m][n]

# Example usage
word1 = "yitten"
word2 = "zitting"
distance = levenshtein_distance(word1, word2)
print(f"The Levenshtein distance between '{word1}' and '{word2}' is {distance}")
