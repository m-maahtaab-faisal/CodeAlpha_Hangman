import random
import os

def clear_screen():
    """Clears the terminal for a smooth, static UI frame."""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_hangman_art(tries: int) -> str:
    """Returns heavy block ASCII art based on remaining tries."""
    stages = [
        # 0 Tries left: DEAD
        """
           ▄▄▄▄▄▄▄▄▄▄▄▄▄
           █           ▼
           █         (X_X)
           █          /█\\ 
           █          / \\ 
           █
        ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
        """,
        # 1 Try left
        """
           ▄▄▄▄▄▄▄▄▄▄▄▄▄
           █           ▼
           █         (O_O)
           █          /█\\ 
           █          /  
           █
        ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
        """,
        # 2 Tries left
        """
           ▄▄▄▄▄▄▄▄▄▄▄▄▄
           █           ▼
           █         (O_O)
           █          /█\\ 
           █          
           █
        ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
        """,
        # 3 Tries left
        """
           ▄▄▄▄▄▄▄▄▄▄▄▄▄
           █           ▼
           █         (O_O)
           █          /█  
           █          
           █
        ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
        """,
        # 4 Tries left
        """
           ▄▄▄▄▄▄▄▄▄▄▄▄▄
           █           ▼
           █         (O_O)
           █           █  
           █          
           █
        ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
        """,
        # 5 Tries left
        """
           ▄▄▄▄▄▄▄▄▄▄▄▄▄
           █           ▼
           █         (O_O)
           █            
           █          
           █
        ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
        """,
        # 6 Tries left: Initial State
        """
           ▄▄▄▄▄▄▄▄▄▄▄▄▄
           █           ▼
           █           
           █            
           █          
           █
        ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
        """
    ]
    return stages[tries]

def print_ui(tries: int, word_completion: list, guessed_letters: list, message: str = "") -> None:
    """Handles the rendering of the heavy UI frame."""
    clear_screen()
    print("▀" * 45)
    print("               H A N G M A N                 ")
    print("▄" * 45)
    
    print(get_hangman_art(tries))
    
    # Display the word with spaces
    print(f"   TARGET:  {' '.join(word_completion)}")
    print("-" * 45)
    
    # Display stats
    print(f"   TRIES LEFT:  {tries}")
    print(f"   INTEL:       {', '.join(sorted(guessed_letters))}")
    print("▀" * 45)
    
    if message:
        print(f"   >> {message}")
        print("▄" * 45)

def main():
    # CodeAlpha Requirement: 5 predefined words
    words = ["PYTHON", "GITHUB", "CODING", "INTERN", "SCRIPT"]
    secret_word = random.choice(words)
    
    guessed_letters = []
    word_completion = ["_"] * len(secret_word)
    tries = 6 # CodeAlpha Requirement: Limit incorrect guesses to 6[cite: 1]
    message = "System initialized. Enter your first guess."
    
    while tries > 0 and "_" in word_completion:
        print_ui(tries, word_completion, guessed_letters, message)
        
        guess = input("\n   Enter a letter: ").upper().strip()
        
        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            message = "ERROR: Invalid input. Single alphabetical characters only."
            continue
            
        if guess in guessed_letters:
            message = f"WARNING: Intel already acquired on '{guess}'."
            continue
            
        guessed_letters.append(guess)
        
        # Incorrect guess
        if guess not in secret_word:
            tries -= 1
            message = f"CRITICAL: '{guess}' not found in target."
        # Correct guess
        else:
            message = f"SUCCESS: '{guess}' confirmed in target."
            for i, letter in enumerate(secret_word):
                if letter == guess:
                    word_completion[i] = guess

    # Final screen rendering
    print_ui(tries, word_completion, guessed_letters)
    
    if "_" not in word_completion:
        print("\n   [ MISSION ACCOMPLISHED: TARGET IDENTIFIED ]\n")
    else:
        print(f"\n   [ MISSION FAILED: TARGET WAS '{secret_word}' ]\n")

if __name__ == "__main__":
    main()