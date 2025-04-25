
def palindrome(string, idx):
    def find_palindrome(word, index):
        if index == len(word):
            return ''
        return word[- 1 -index] + find_palindrome(word, index + 1)

    reversed_word = find_palindrome(string, idx)

    if reversed_word == string:
        return f'{string} is a palindrome'
    return f'{string} is not a palindrome'


print(palindrome("tenet", 0))