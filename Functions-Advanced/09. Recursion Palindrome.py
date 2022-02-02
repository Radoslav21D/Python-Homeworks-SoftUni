def palindrome(word, idx):
    if idx == len(word) // 2:
        return f'{word} is a palindrome'
    if word[idx] != word[len(word) - 1 - idx]:
        return f'{word} is not a palindrome'
    return palindrome(word, idx + 1)


print(palindrome("abcba", 0))
print(palindrome("peter", 0))

# word = 'abcba'
#
# is_palindrome = True
#
# for i in range(len(word) // 2):
#     if word[i] != word[len(word) - 1 - i]:
#         is_palindrome = False
#         break
#
# print(is_palindrome)
