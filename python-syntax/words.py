
def print_upper_words(words, must_start_with=None):
    """Print each word on a separate line in uppercase.

    If must_start_with is provided, only words that start with one of the given letters will be printed.
    - words: list of words
    - must_start_with: set of letters (case-insensitive)

    """

    for word in words:
        if must_start_with:
            if word[0].lower() in must_start_with:
                print(word.upper())
        else:
            print(word.upper())


# 1. Print each word in uppercase
words = ['hello', 'hey', 'goodbye', 'yo', 'yes']
for word in words:
    print(word.upper())

# 2. Test the function without filtering letters
print('\nPrint all words in uppercase:')
print_upper_words(words)

# 3. Test the function to only print words that start with 'e'
print('\nPrint words that start with e or E:')
print_upper_words(words, must_start_with={'e'})

# 4. Test the function with a set of letters
print('\nPrint words that start with h or g:')
print_upper_words(words, must_start_with={'h', 'g'})
