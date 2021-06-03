started = False
while True:
    command = input(">  ").lower()
    if command == "start":
         if started:
             print("already started ")
         else:
             started = True
             print("engine started")
    elif command == "stop":
        if not started:
            print("already stopped")
        else:
            started = False

            print("the engine has been stopped  ")
    elif command == "help":
        print("""
        start- to start the engine
        stop- to stop the engine
        quit- to stop the game
        """)
    elif command == "quit":
        break
    else:
        print("i do not understand what you are trying to do ")


