import random

def choose_word():
    words = ['python', 'programming', 'developer', 'challenge', 'game', 'function', 'variable', 'loop', 'condition', 'algorithm', 'data', 'structure', 'object', 'class', 'method', 'inheritance', 'polymorphism', 'encapsulation', 'abstraction', 'interface', 'module', 'package', 'library', 'framework', 'syntax', 'debugging', 'testing', 'exception', 'recursion', 'iteration', 'array', 'list', 'dictionary', 'tuple', 'set', 'string', 'integer', 'float', 'boolean', 'operator', 'expression', 'statement', 'parameter', 'argument', 'return', 'lambda', 'decorator', 'generator', 'comprehension', 'context', 'manager', 'thread', 'process', 'concurrency', 'parallelism', 'asynchronous', 'synchronous', 'event', 'callback', 'promise', 'future', 'await', 'yield', 'closure', 'scope', 'namespace', 'global', 'local', 'nonlocal', 'mutable', 'immutable', 'hash', 'key', 'value', 'pair', 'dictionary', 'set', 'list', 'tuple', 'array', 'matrix', 'vector', 'graph', 'tree', 'node', 'edge', 'path', 'cycle', 'connected', 'disconnected', 'weighted', 'unweighted', 'directed', 'undirected', 'algorithm', 'complexity', 'big O', 'big theta', 'big omega', 'sorting', 'searching', 'traversal', 'dynamic programming', 'greedy', 'divide and conquer', 'backtracking', 'branch and bound', 'memoization', 'recursion', 'iteration', 'loop', 'condition', 'statement', 'expression', 'function', 'method', 'class', 'object',]
    return random.choice(words)

def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def play_game():
    word = choose_word()
    guessed_letters = set()
    attempts = 6

    print("¡Bienvenido al juego de adivinanza de palabras!")
    print("Adivina la palabra letra por letra.")

    while attempts > 0:
        print(f"\nPalabra: {display_word(word, guessed_letters)}")
        print(f"Intentos restantes: {attempts}")
        guess = input("Adivina una letra: ").lower()

        if guess in guessed_letters:
            print("Ya has adivinado esa letra. Intenta con otra.")
        elif guess in word:
            guessed_letters.add(guess)
            print("¡Bien hecho! Esa letra está en la palabra.")
        else:
            attempts -= 1
            print("Lo siento, esa letra no está en la palabra.")

        if all(letter in guessed_letters for letter in word):
            print(f"\n¡Felicidades! Has adivinado la palabra: {word}")
            break
    else:
        print(f"\nTe has quedado sin intentos. La palabra era: {word}")

if __name__ == "__main__":
    play_game()
