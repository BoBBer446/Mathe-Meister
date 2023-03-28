import random
import config
import storage
import time
import cli

def insert_parentheses(expression):
    tokens = expression.split()
    
    if len(tokens) <= 2:
        return expression

    operator_positions = [i for i, token in enumerate(tokens) if token in "+-*/"]
    if len(operator_positions) < 2:
        return expression

    selected_operator_position = random.choice(operator_positions[:-1])
    start = selected_operator_position - 1
    end = selected_operator_position + 4

    return " ".join(tokens[:start] + ["("] + tokens[start:end] + [")"] + tokens[end:])


def generate_math_problem(level):
    level_settings = config.LEVEL_SETTINGS[level]
    operations = level_settings["operations"]
    max_value = level_settings["max_value"]
    min_value = level_settings["min_value"]
    num_operands = level_settings["num_operands"]

    problem = ""
    correct_answer = max_value + 1  # Initialisierung mit einem Wert außerhalb des gültigen Bereichs

    while correct_answer > max_value or correct_answer < min_value:
        problem = ""
        for i in range(num_operands - 1):
            if i == 0:
                problem += str(random.randint(min_value, max_value))
            problem += " " + random.choice(operations) + " "
            problem += str(random.randint(min_value, max_value))

        if "()" in operations:
            problem = insert_parentheses(problem)

        correct_answer = round(eval(problem), 2)

    return problem, correct_answer




def check_answer(user_answer, correct_answer):
    try:
        return int(user_answer) == correct_answer
    except ValueError:
        return False

def start_game(username):
    print(f"Spiel gestartet für {username}!")

    current_level = 1
    points = 0
    total_incorrect_attempts = 0
    total_correct_answers = 0
    total_time = 0

    while current_level <= 15:
        print(f"\nLevel {current_level}")

        for question_number in range(10):
            problem, correct_answer = generate_math_problem(current_level)
            attempts = 3

            start_time = time.time()

            while attempts > 0:
                user_answer = cli.display_question(question_number, problem)

                if check_answer(user_answer, correct_answer):
                    print("Richtig!")
                    points += 1
                    total_correct_answers += 1
                    break
                else:
                    attempts -= 1
                    total_incorrect_attempts += 1

                    if total_incorrect_attempts >= 10:
                        print("Du hast 10 falsche Antworten erreicht. Das Spiel ist beendet.")
                        print(f"Deine Punktzahl: {points}")
                        storage.save_score(username, points, total_correct_answers, total_incorrect_attempts, total_time)
                        return

                    cli.display_result(False, attempts, correct_answer)

                if attempts == 0:
                    cli.display_result(False, 0, correct_answer)

            end_time = time.time()
            total_time += (end_time - start_time)

        current_level += 1

    cli.display_game_over(points)
    storage.save_score(username, points, total_correct_answers, total_incorrect_attempts, total_time)
