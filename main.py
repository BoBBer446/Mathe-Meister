#main.py: Dies ist die Hauptdatei deines Spiels, in der du die Anwendung initialisierst und startest. 
#Sie beinhaltet auch den Hauptteil der Spiellogik und steuert den Ablauf des Spiels.
#
#game_logic.py: In dieser Datei organisierst du die gesamte Spiellogik und die verwendeten Funktionen. 
#Dazu gehören die Generierung von Aufgaben, die Überprüfung der Antworten, die Verwaltung von Leveln und die Speicherung von Spielerdaten.
#
#cli.py: In dieser Datei implementierst du die Funktionen, die für die Interaktion mit dem Benutzer über die Kommandozeile verantwortlich sind. 
#Dazu gehören das Anzeigen von Menüs, das Ausgeben von Aufgaben und das Einlesen von Benutzereingaben.
#
#config.py: In dieser Datei legst du verschiedene Einstellungen und Konfigurationswerte für das Spiel fest, wie z.B. die Anzahl der Level, 
#die Anzahl der Versuche pro Aufgabe, die Punktevergabe und andere spielrelevante Informationen.
#
#storage.py: In dieser Datei implementierst du die Funktionen zum Speichern und Abrufen von Spielerdaten und Highscores in einer lokalen Datei. 
#Du kannst beispielsweise das pickle-Modul oder das json-Modul in Python verwenden, um die Daten zu


import game_logic
import cli
import storage

def main():
    print("Willkommen beim Mathe-Meister!")
    
    while True:
        cli.display_menu()
        user_choice = cli.get_user_choice()
        
        if user_choice == "1":
            username = cli.select_user()
            game_logic.start_game(username)
        elif user_choice == "2":
            highscores = storage.load_highscores()
            cli.display_highscores(highscores)
        elif user_choice == "3":
            print("Danke fürs Spielen! Auf Wiedersehen.")
            break
        else:
            print("Ungültige Eingabe. Bitte wähle eine Option zwischen 1 und 3.")

if __name__ == "__main__":
    main()

