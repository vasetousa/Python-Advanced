text = input().split(', ')

result = [f"{word} -> {len(word)}" for word in text]
print(', '.join(result))