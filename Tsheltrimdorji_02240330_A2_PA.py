import random

class GameCollection:
    def __init__(self):
        self.games = {
            1: "Guess Number Game",
            2: "Rock-Paper-Scissors",
            3: "Trivia Pursuit Quiz",
            4: "Pokémon Card Binder Manager",
            5: "Overall Scoring"
        }
    
    def display_menu(self):
        print("\nSelect a game:")
        for num, game in self.games.items():
            print(f"{num}. {game}")
        print("6. Exit")
    
    def guess_number_game(self):
        number_to_guess = random.randint(1, 100)
        attempts = 0
        print("Welcome to the Guess Number Game! Guess a number between 1 and 100.")
        
        while True:
            guess = int(input("Enter your guess: "))
            attempts += 1
            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                return attempts  # Return the number of attempts as a score
    
    def rock_paper_scissors(self):
        choices = ["rock", "paper", "scissors"]
        print("Welcome to Rock-Paper-Scissors!")
        wins = 0
        
        while True:
            user_choice = input("Enter rock, paper, or scissors (or 'exit' to quit): ").lower()
            if user_choice == 'exit':
                break
            if user_choice not in choices:
                print("Invalid choice. Please try again.")
                continue
            
            computer_choice = random.choice(choices)
            print(f"Computer chose: {computer_choice}")
            
            if user_choice == computer_choice:
                print("It's a tie!")
            elif (user_choice == "rock" and computer_choice == "scissors") or \
                (user_choice == "paper" and computer_choice == "rock") or \
                (user_choice == "scissors" and computer_choice == "paper"):
                print("You win!")
                wins += 1
            else:
                print("You lose!")
        
        return wins  # Return the number of wins as a score
    
    def trivia_quiz(self):
        questions = {
            "What is the capital of France?": ["a) Paris", "b) London", "c) Berlin", "d) Madrid"],
            "What is 2 + 2?": ["a) 3", "b) 4", "c) 5", "d) 6"],
            "What is the largest planet in our solar system?": ["a) Earth", "b) Mars", "c) Jupiter", "d) Saturn"]
        }
        
        correct_answers = {
            "What is the capital of France?": "a",
            "What is 2 + 2?": "b",
            "What is the largest planet in our solar system?": "c"
        }
        
        score = 0
        print("Welcome to the Trivia Pursuit Quiz!")
        
        for question, options in questions.items():
            print(question)
            for option in options:
                print(option)
            answer = input("Enter your answer (a, b, c, or d): ").lower()
            
            if answer == correct_answers[question]:
                print("Correct!")
                score += 1
            else:
                print("Wrong answer.")
        
        print(f"Your total score is: {score}/{len(questions)}")
        return score  # Return the quiz score
    
    def overall_scoring(self):
        print("Overall Scoring:")
        print("1. Guess Number Game: 1 point for winning.")
        print("2. Rock-Paper-Scissors: 1 point for winning.")
        print("3. Trivia Pursuit: 1 point for each correct answer.")
        print("4. Pokémon Card Binder: No scoring, just management.")
    
    def run(self):
        while True:
            self.display_menu()
            try:
                choice = int(input("Enter your choice: "))
                
                if choice == 1:
                    self.guess_number_game()
                elif choice == 2:
                    self.rock_paper_scissors()
                elif choice == 3:
                    self.trivia_quiz()
                elif choice == 4:
                    print("Pokémon Card Binder Manager is not implemented yet.")
                elif choice == 5:
                    self.overall_scoring()
                elif choice == 6:
                    print("Goodbye!")
                    break
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Please enter a number between 1 and 6.")

# Main execution
if __name__ == "__main__":
    game_collection = GameCollection()
    game_collection.run()