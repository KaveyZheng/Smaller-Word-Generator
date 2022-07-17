user_word = input("Enter a word: ").lower()
word_dict = {letter: user_word.count(letter) for letter in set(user_word)}

# List of words shorter than user_word
smaller_words = []
with open("words_alpha.txt") as file:
  for word in file:
    word = word.strip()
    if len(word) < len(user_word):
      smaller_words.append(word)

# List of words with the same letters as user_word from smaller_words
similar_letters = []
for word in smaller_words:
  for letter in word:
    if letter in user_word:
      match = True
    else:
      match = False
      break
  if match:
    similar_letters.append(word)

# List of possible words from similar_letters
possible_words = []
for word in similar_letters:
  for letter in word:
    if word_dict[letter] - word.count(letter) < 0:
      match = False
      break
    else:
      match = True
  if match:
    possible_words.append(word)

print("")
for word in possible_words:
  print(f"Possible Word: {word}")