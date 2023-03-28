def display_menu():
    print("\nHauptmenü:")
    print("1. Neues Spiel starten")
    print("2. Highscores anzeigen")
    print("3. Spiel beenden")


def get_user_choice():
    return input("Wähle eine Option (1-3): ")


def display_level(level):
    print(f"\nLevel {level}")


def display_question(question_number, problem):
    return input(f"Frage {question_number + 1}: {problem} = ")


def display_result(is_correct, attempts_remaining, correct_answer):
    if is_correct:
        print("Richtig!")
    elif attempts_remaining > 0:
        print(f"Falsch! Versuche es erneut. Die richtige Antwort wäre {correct_answer} gewesen.")
    else:
        print(f"Keine Versuche mehr übrig. Die richtige Antwort wäre {correct_answer} gewesen.")


def display_correct_answer(correct_answer):
    print(f"Die richtige Antwort wäre {correct_answer} gewesen.")


def display_game_over(points):
    print(f"Spiel beendet! Du hast {points} Punkte erreicht.")


def display_highscores(highscores):
    print("\nHighscores:")
    for index, score in enumerate(highscores, start=1):
        print(f"{index}. {score['username']}: {score['points']} Punkte")
        if 'total_correct' in score:
            total_time = score['total_time']
            minutes = int(total_time / 60)
            seconds = total_time % 60
            print(f"    Richtig beantwortet: {score['total_correct']}")
            print(f"    Falsch beantwortet: {score['total_incorrect']}")
            print(f"    Gesamtzeit: {minutes} Minuten und {seconds:.2f} Sekunden")
            print(f"    Datum: {score['date']}")


def select_user():
    users = ["Rene", "Milan", "Juliane", "Ole", "Mattis"]
    print("\nWähle einen Benutzer aus:")
    for index, user in enumerate(users, start=1):
        print(f"{index}. {user}")
    user_choice = int(input("Wähle eine Option (1-5): "))
    return users[user_choice - 1]
