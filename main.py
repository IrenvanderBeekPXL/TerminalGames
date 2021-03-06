# The games programmed in here do not use the GPU and only 1 core

import os
pythongames = ["hartenjagen", "memory", "OXO", "quiz", "schaken", "zeeslag", "hangman",
               "MensErgerJeNiet", "MensErgerJeNietAI", "racko"]
javagames = ["hoogsteKaart", "UNO"]
games = pythongames + javagames
print("Welcome to TerminalGames")
print("Some games only work on 1920 * 1080 resolution")
print("Copy one of the following games")
for i in games:
    print(i)
try:
    game = input("Which game do you want to play?")
    while game != "stop":
        print("Opening game...")
        if game in pythongames:
            os.system("python3 " + game + "/main.py")
        elif game in javagames:
            os.system("java -jar " + game + "/main.jar")
        print("Copy one of the following games")
        for i in games:
            print(i)
        game = input("Which game do you want to play?")
except KeyboardInterrupt:
    print("Please don't Ctrl+C out. Use the stop command instead")