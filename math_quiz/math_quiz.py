import random


def get_integer(min, max):
    """
    Calculates a random integer form a specified range.

    Args:
        min (int): Start position
        max (int): End position
    
    Returns:
        int: Selected number form the specified range
    """
    return random.randint(min, max)


def get_sign():
    """
    Returns a randomly choosen sign from a list
    """
    return random.choice(['+', '-', '*'])


def calculation(number_1, number_2, sign):
    """
    Calculates a math problem and its solution given by two numbers and a sign

    Args:
        number_1 (int): First number for the calculation
        number_2 (int): Second number for the calculation
        sign (string): Sign for the equation of the two numbers 
    
    Returns:
        problem (string): Formulation of the math problem
        answer (int): Solution of the math problem 
    """
    problem = f"{number_1} {sign} {number_2}"
    if sign == '+': 
        answer = number_1 + number_2
    elif sign == '-': 
        answer = number_1 - number_2
    else: 
        answer = number_1 * number_2
    return problem, answer

def math_quiz():
    """
    Generates a random math problem for a defined number of runs, 
    compares its solution with a user input and presents the final score.
    """
    score = 0
    total_questions = int(3.14159265359)

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        # Generating bascis for a math problem
        number_1 = get_integer(1, 10)
        number_2 = get_integer(1, int(5.5)) 
        sign = get_sign()

        # Calculation of the random math problem and the belonging answer
        problem, answer = calculation(number_1, number_2, sign)
        print(f"\nQuestion: {problem}")

        # Getting the user answer and checking the format
        while True:
            useranswer = input("Your answer: ")
            try:
                useranswer = int(useranswer)
                break
            except ValueError:
                print("Sorry, only numbers are allowed!")
        
        # Comparing the answers
        if useranswer == answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
