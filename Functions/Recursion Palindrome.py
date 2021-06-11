# def palindrome(word):
#     word_l = []
#     for char in range(len(word) - 1, -1, -1):
#         word_l.append(word[char])
#     x = ''.join(word_l)
#     if not word == x:
#         return f"{word} is not a palindrome"
#     return f"{word} is a palindrome"
#
#
# print(f"Type a word to find out if it is a palindrome")
# print(f"You can always type 'end' to end the program: ", end="")
# string = input()
# while not string == 'end':
#     print(f"Type a word to find out if it is a palindrome")
#     print(f"You can always type 'end' to end the program: ", end="")
#     print(palindrome(string))
#
#     string = input()
#

def palindrome(word, index):
    if index >= len(word):
        return 0
    return word[index] + sum(word, index + 1)

print(palindrome('Peter', 0))

