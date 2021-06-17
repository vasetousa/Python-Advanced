def get_words(file_path):
    with open(file_path, 'r') as file:
        return file.read().split()

def get_words_counts(file_path, words):
    words_counts = { word: 0 for word in words }
    with open(file_path, 'r') as file:
        for line in file:
            words_in_line = line.lower().split()
            for word in words:
                words_counts[word] += words_in_line.count(word)
                if word in line.lower():
                    words_counts[word] += 1
    return words_counts

words_file_path = './words'
text_file_path = './text'

words_counts = get_words_counts(text_file_path, get_words(words_file_path))
print(words_counts)