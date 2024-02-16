#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#  Spell check
# ---------------------------------------------------------------------------
# 
#
##############################################################################

#==============================================================================
# In separate chaining, each bucket in the hash table is a linked list.
class LinkedListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

#==============================================================================
# HashTable function 
# implementation of a hash table using separate chaining to handle collisions:
#----------------------------------------------------------------
# 1) Insert a word, put(key, value)
# 2) search a word, get(key)
#==============================================================================
class HashTable:
    def __init__(self, size):
        self.size = size
        self.buckets = [None] * size

    def _hash_function(self, key):
        return hash(key) % self.size

  def put(self, key):
        index = self._hash_function(key)
        if self.buckets[index] is None:
            self.buckets[index] = LinkedListNode(key, None)  # set value None
        else:
            node = self.buckets[index]
            while node.next:
                node = node.next
            node.next = LinkedListNode(key, None) 

    def get(self, key):
        index = self._hash_function(key)
        node = self.buckets[index]
        while node:
            if node.key == key:
                return node.value
            node = node.next
        return None

# ===============================================================
# 4）Levenshtein distance algorithm to compute the edit distance between two words.
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

# ===============================================================
# 1）load a file and read word from the file 
def load_dictionary(file_path):
    words = set()
    with open(file_path, 'r') as file:
        for line in file:
            words.update(line.strip().lower().split())
    return words

# 2）spell check for the hash table 
def spell_check(text, dictionary, hash_table):
    misspelled = []
    for word in text.lower().split():
        if word not in dictionary:
            suggestions = suggest_corrections(word, dictionary)
            misspelled.append((word, suggestions))
    return misspelled

# 3）check word and distance for suggestion
def suggest_corrections(word, dictionary):
    threshold = 2  # Maximum edit distance for suggestions
    return [w for w in dictionary if levenshtein_distance(word, w) <= threshold]

# 4）update hash table dictionary
def update_dictionary(word, dictionary, hash_table):
    dictionary.add(word)
    hash_table.put(word)

#===============================================================================
# main function 
# 
def main():
    # [1] read words from dictionary file and insert hash table
    dictionary_file = 'words.txt'
    dictionary = load_dictionary(dictionary_file)
    hash_table = HashTable(len(dictionary))
    for word in dictionary:
        hash_table.put(word)

    # [2] spell check and print out words suggestions 
    text_to_check = "Thiss is a smple text with some misspeled words"
    misspelled_words = spell_check(text_to_check, dictionary, hash_table)
    print("Misspelled words and suggestions:")
    for word, suggestions in misspelled_words:
        print(f"{word}: {', '.join(suggestions)}")

    # [3] if words misspeled, added to hash table
    new_word = "misspeled"
    update_dictionary(new_word, dictionary, hash_table)
    print(f"Added '{new_word}' to the dictionary.")


# ================================================================================
if __name__ == "__main__":
    main()
