# Check if two words are anagrams
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    word = input("Enter your first word\n")
    anagram = input("Enter your second word\n")

    if sorted(word) == sorted(anagram):
        print("True, that's an anagram there")
        return True
    else:
        print("False, no anagram detected")
        return False


find_anagram('word', 'anagram')
