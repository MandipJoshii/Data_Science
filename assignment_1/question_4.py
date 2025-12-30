# Ask the user to input a word and count vowels and consonants using a function.

def vowel_consonant():
    word = input("ENTER A WORD: ").lower()

    vowel = "aeiou"

    vowel_count = 0
    consonent_count = 0

    for char in word:
        if char in vowel:
            vowel_count += 1
        else:
            consonent_count += 1

    print("vowel", vowel_count)
    print("consonent", consonent_count)

vowel_consonant()