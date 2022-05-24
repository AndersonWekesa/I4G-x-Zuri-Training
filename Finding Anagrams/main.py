# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


def find_anagrams(word1, word2):
    # [assignment] Add your code here

    first_word = word1.lower()      #Make both words lowercase in order to compare them
    second_word = word2.lower()

    if sorted(first_word) == sorted(second_word): #Sort characters of both strings alphabetically and see if they match
        IsAnagram = True
    else:
        IsAnagram = False

    return IsAnagram

#Test the Function
print(find_anagrams("night", "thing")) #Returns True
print(find_anagrams("hello", "world")) #Returns False

