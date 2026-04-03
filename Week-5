def start_quize():
    quiz = {
    "Capital of India?": "delhi",
    "5 + 7 = ?": "12",
    "Color of sky?": "blue"
    }

    score = 0  
    while True:
        for questions in quiz:
            print(questions)

            answer = input("Answer: ").lower()
            if answer == quiz[questions]:
                score += 1
            else:
                print("The right answer is", quiz[questions])

        print(f"You scored {score} out of {len(quiz)}")

        play_again = input("Do you want to play again? (y/n)").lower()
        if play_again == "y":
            continue
        
        elif play_again == "n":
            print("Thank you for playing")
        break
        
start_quize()
