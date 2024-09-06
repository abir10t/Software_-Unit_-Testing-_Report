import random
import time
import string
import enchant  # Library to check valid words

# Initialize English dictionary
d = enchant.Dict("en_US")

# Scrabble letter scores
SCORES = {
    1: "AEIOULNRST",
    2: "DG",
    3: "BCMP",
    4: "FHVWY",
    5: "K",
    8: "JX",
    10: "QZ"
}

# Function to calculate scrabble score for a given word
def scrabble_score(word):
    score = 0
    word = word.upper()

    for letter in word:
        if letter.isalpha():  # Only consider alphabetical characters
            for points, letters in SCORES.items():
                if letter in letters:
                    score += points
                    break
    return score

# Function to check if a word is valid using a dictionary
def is_valid_word(word):
    return d.check(word)

# Function to check if the entered word has the correct length
def word_length_is_correct(word, expected_length):
    return len(word) == expected_length

# Main function to handle the game loop
def play_game():
    total_score = 0
    rounds = 10
    print("Welcome to the Scrabble Score Game!")
    
    for round_num in range(1, rounds + 1):
        print(f"\nRound {round_num}:")
        
        # Randomly generate the required word length
        word_length = random.randint(3, 7)
        print(f"Enter a word with exactly {word_length} letters. You have 15 seconds to submit.")
        
        start_time = time.time()  # Start the timer
        
        while True:
            word = input("Your word: ").strip()

            # Check if word has the correct length
            if not word_length_is_correct(word, word_length):
                print(f"Word must have exactly {word_length} letters. Try again.")
                continue
            
            # Check if the word is valid in the dictionary
            if not is_valid_word(word):
                print("Invalid word. Please enter a valid word.")
                continue

            # Check the time taken
            time_taken = time.time() - start_time
            if time_taken > 15:
                print("Time exceeded! No score for this round.")
                break

            # Calculate score and bonus for quick submission
            round_score = scrabble_score(word)
            time_bonus = max(0, 15 - int(time_taken))  # Bonus for quicker inputs
            total_score += round_score + time_bonus

            print(f"Score for the word: {round_score}. Time bonus: {time_bonus}")
            print(f"Total score so far: {total_score}")
            break
    
    print(f"Game over! Your total score after {rounds} rounds is: {total_score}")

if __name__ == '__main__':
    play_game()