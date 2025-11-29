import random
answers = []
guesses = []
results = []  
while True:
    answer = random.randint(1, 2)
    guess = input("Enter your guess as 1 for head, 2 for tail, or 0 to exit: ")
    if not guess.isdigit():
        print("Please enter 0, 1, or 2.\n")
        continue
    guess = int(guess)
    if guess == 0:
        print("Thank you for playing the game!\n")
        break
    if guess not in [1, 2]:
        print("Please enter 0, 1, or 2.\n")
        continue
    answers.append(answer)
    guesses.append(guess)
    if answer == guess:
        print("Correct!\n")
        results.append(True)
    else:
        print("Wrong!\n")
        results.append(False)
correct = sum(results)
incorrect = len(results) - correct
print("Result")
print("--------")
print(f"You have made {correct} correct guess{'es' if correct != 1 else ''}", end=" ")
print(f"and {incorrect} incorrect guess{'es' if incorrect != 1 else ''}.\n")
for i in range(len(answers)):
    print(f"Round #{i+1}")
    print("Answer:  {}".format("Head" if answers[i] == 1 else "Tail"))
    print("Guess:   {}".format("Head" if guesses[i] == 1 else "Tail"))
    print("Result:  {}\n".format("Correct" if results[i] else "Wrong"))