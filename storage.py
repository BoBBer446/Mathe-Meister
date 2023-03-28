# Diese Funktion speichert die Punktzahl eines Benutzers zusammen mit seinen anderen Daten in einer lokalen JSON-Datei.
# Der Funktion werden der Benutzername, die erreichten Punkte, die Anzahl der korrekten Antworten, die Anzahl der falschen Antworten und die Gesamtzeit des Spiels übergeben.
# Die aktuelle Zeit wird auch erfasst und in das Ergebnis eingefügt.
# Die Funktion ruft die Funktion "load_highscores()" auf, um die aktuell in der Datei gespeicherten Highscores zu laden.
# Anschließend wird das neue Score-Objekt in die Highscores-Liste hinzugefügt und die Liste nach Punktzahl sortiert.
# Schließlich wird die aktualisierte Liste in die Datei gespeichert.
# Diese Funktion lädt die Highscores aus der lokalen JSON-Datei.
# Wenn die Datei nicht existiert, gibt die Funktion eine leere Liste zurück.
# Andernfalls wird die Liste aus der Datei geladen und zurückgegeben.

import json
import os
import datetime

SCORES_FILE = "highscores.json"

def save_score(username, points, total_correct, total_incorrect, total_time):
    highscores = load_highscores()
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    
    score_data = {
        'username': username,
        'points': points,
        'total_correct': total_correct,
        'total_incorrect': total_incorrect,
        'total_time': total_time,
        'date': current_date,
    }
    
    highscores.append(score_data)
    highscores.sort(key=lambda x: x['points'], reverse=True)

    with open(SCORES_FILE, "w") as file:
        json.dump(highscores, file)

def load_highscores():
    if not os.path.exists(SCORES_FILE):
        return []

    with open(SCORES_FILE, "r") as file:
        highscores = json.load(file)
    
    return highscores
