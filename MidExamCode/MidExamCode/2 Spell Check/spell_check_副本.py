#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#  Spell check
# ---------------------------------------------------------------------------
# 
#
##############################################################################

import Levenshtein

#================================================================
# HashTable function 
#----------------------------------------------------------------
# 1) Insert a word
# 2) search a word
#================================================================
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, word):
        return len(word) % self.size

    def insert(self, word):
        index = self.hash_function(word)
        self.table[index].append(word)

    def search(self, word):
        index = self.hash_function(word)
        return word in self.table[index]

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
    return [w for w in dictionary if Levenshtein.distance(word, w) <= threshold]

# 4）update hash table dictionary
def update_dictionary(word, dictionary, hash_table):
    dictionary.add(word)
    hash_table.insert(word)


#===============================================================================
# main function 
# 
def main():
    # [1] read words from dictionary file and insert hash table
    dictionary_file = 'words.txt'
    dictionary = load_dictionary(dictionary_file)
    hash_table = HashTable(len(dictionary))
    for word in dictionary:
        hash_table.insert(word)

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
