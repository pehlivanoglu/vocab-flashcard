# Flashcard Vocab Game
This is a simple Python-based flashcard game designed to help you memorize English words. The game reads words and their descriptions from a file, quizzes you on them, and tracks which words you’ve already answered correctly.
I needed a game like this while I was studying for IELTS, so I made myself one in 15 minutes :) 

### Playing the Game
- To start the flashcard game: ```python3 main.py```
- To reset the used words: ```python3 main.py reset```

### Vocabulary File (vocab.txt)
The vocab.txt file should contain words and their descriptions in the following format:
```
word1:description1
word2:description2
word3:description3
```

When you answer a word correctly, it will be marked as used by adding a - prefix, thus it will not be used until all words are asked:
```
-apple:elma
table:masa
```