

# Anzahl der Level
LEVEL_COUNT = 15

# Anzahl der Versuche pro Aufgabe
ATTEMPTS_PER_QUESTION = 3

# Punkte pro richtig gelöster Aufgabe
POINTS_PER_CORRECT_ANSWER = 1

# Level-Einstellungen
LEVEL_SETTINGS = {
    1: {"operations": ["+"], "max_value": 10, "min_value": 0, "num_operands": 2},
    2: {"operations": ["-"], "max_value": 10, "min_value": 0, "num_operands": 2},
    3: {"operations": ["+"], "max_value": 20, "min_value": 0, "num_operands": 2},
    4: {"operations": ["+", "-"], "max_value": 50, "min_value": 0, "num_operands": 2},
    5: {"operations": ["+", "-"], "max_value": 100, "min_value": 0, "num_operands": 2},
    6: {"operations": ["+", "-", "*", "/"], "max_value": 100, "min_value": 0, "num_operands": 2},
    7: {"operations": ["+", "-", "*", "/", "%"], "max_value": 100, "min_value": 0, "num_operands": 2},
    8: {"operations": ["+", "-", "*", "/", "%"], "max_value": 200, "min_value": 0, "num_operands": 2},
    9: {"operations": ["+", "-", "*", "/", "%"], "max_value": 300, "min_value": 0, "num_operands": 2},
    10: {"operations": ["+", "-", "*", "/", "%"], "max_value": 500, "min_value": 0, "num_operands": 2},
    11: {"operations": ["+", "-", "*", "/", "%"], "max_value": 500, "min_value": 0, "num_operands": 3},
    12: {"operations": ["+", "-", "*", "/", "%"], "max_value": 1000, "min_value": 0, "num_operands": 3},
    13: {"operations": ["+", "-", "*", "/", "%"], "max_value": 1000, "min_value": 0, "num_operands": 4},
    14: {"operations": ["+", "-", "*", "/", "%"], "max_value": 2000, "min_value": 0, "num_operands": 4},
    15: {"operations": ["+", "-", "*", "/", "%", "()"], "max_value": 5000, "min_value": 0, "num_operands": 4},
}

# Pfad zur lokalen Datei für die Speicherung von Spielerdaten und Highscores
DATA_FILE_PATH = "data_file.json"
