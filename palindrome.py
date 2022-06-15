def get():
    return input("word: ")


def reverse(word):
    return word[::-1]


def get_num_matched_chars(word, revers):
    match = 0
    for i in range(0, len(word)):
        if revers[i] == word[i]:
            match = match + 1
    return match


given = get()


def check_palindrome(word):
    if get_num_matched_chars(given, reverse(given)) == len(word):
        print("is a palindrome")
    else:
        print("not a palindrome.")


check_palindrome(given)
