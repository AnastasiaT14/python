sentences = []

for i in range(5):
    sentence = str(input("Enter the sentence "))
    sentences.append(sentence)

longest_string = max(sentences, key=len)

for sentence in sentences:
    print(sentence)
print("\nThe longest sentence is:", longest_string)
