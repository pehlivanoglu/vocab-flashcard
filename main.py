import random
import sys

def load_vocab(file_path):
    with open(file_path, 'r') as file:
        return {line.split(':')[0]: line.split(':')[1].strip() for line in file}

def save_vocab(file_path, vocab):
    with open(file_path, 'w') as file:
        file.writelines([f"{word}:{desc}\n" for word, desc in vocab.items()])

def flashcard_game(vocab, file_path, n):
    words = [word for word in vocab if not word.startswith('-')]
    if not words:
        print("All words have already been used. No words left to test.")
        return

    random.shuffle(words)
    for word in words[:n]:
        answer = input(f"What is the description of '{word}'? ")
        correct_desc = vocab[word]
        if answer.strip().lower() == correct_desc.lower():
            print("Correct!")
            vocab[f"-{word}"] = vocab.pop(word)
            save_vocab(file_path, vocab)
        else:
            print(f"Wrong. The correct description is: {correct_desc}")    

    print("Thank you for playing!")

def reset_vocab(file_path):
    vocab = load_vocab(file_path)
    reset_vocab = {word.lstrip('-'): desc for word, desc in vocab.items()}
    save_vocab(file_path, reset_vocab)
    print("Vocabulary has been reset.")

def main():
    vocab_file = 'vocab.txt'
    
    if len(sys.argv) > 1 and sys.argv[1].lower() == 'reset':
        reset_vocab(vocab_file)
    else:
        vocab = load_vocab(vocab_file)
        n = int(input("How many words would you like to be tested on? "))
        flashcard_game(vocab, vocab_file, n)

if __name__ == "__main__":
    main()
