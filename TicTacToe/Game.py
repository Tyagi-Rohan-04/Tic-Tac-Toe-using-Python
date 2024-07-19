from tkinter import *

root = Tk()
root.geometry("330x550")
root.title("Zero Kata :v")
root.resizable(0,0)

''' Given below are the three frames which are created using tkinter module.
    And they are used to group or organize the other widgets used from the tkinter module.
    Basically they act like the containers for other widgets of tkinter module. '''
frame1 = Frame(root)
frame1.pack()
titleLabel = Label(frame1, text="Zero Kata :*", font=("Arial", 26), bg = "purple", width=16)
titleLabel.grid(row=0, column=0)

optionFrame = Frame(root, bg="grey")
optionFrame.pack()

frame2 = Frame(root, bg="yellow")
frame2.pack()


' Dictionary in which output of the players are stored in a grid form of 3x3. '
board = {1:" ", 2:" ", 3:" ",
         4:" ", 5:" ", 6:" ",
         7:" ", 8:" ", 9:" "}

turn = "x"
game_end = False
mode = "singlePlayer"

' Function to switch to singleplayer game mode. '
def changeModeToSingleplayer():
    global mode
    mode = "singlePlayer"
    singlePlayerButton["bg"] = "orange"
    multiPlayerButton["bg"] = "green"

' Function to switch to multiplayer game mode. '
def changeModeToMultiplayer():
    global mode
    mode = "multiPlayer"
    multiPlayerButton["bg"] = "orange"
    singlePlayerButton["bg"] = "green"

' Function which updates the grid and reset it for a new game event. '
def updateBoard():
    for key in board.keys():
        buttons[key-1]["text"] = board[key]

' Function to check the win condition of the game. '
def checkForWin(player):
    
    # rows winning condition
    if board[1] == board[2] and board[2] == board[3] and board[3] == player:
        return True
    
    elif board[4] == board[5] and board[5] == board[6] and board[6] == player:
        return True
    
    elif board[7] == board[8] and board[8] == board[9] and board[9] == player:
        return True
    
    # column winning condition
    elif board[1] == board[4] and board[4] == board[7] and board[7] == player:
        return True
    
    elif board[2] == board[5] and board[5] == board[8] and board[8] == player:
        return True
    
    elif board[3] == board[6] and board[6] == board[9] and board[9] == player:
        return True
    
    # diagonals winning condition
    elif board[1] == board[5] and board[5] == board[9] and board[9] == player:
        return True
    
    elif board[3] == board[5] and board[5] == board[7] and board[7] == player:
        return True

    return False

' Function to check the draw condition of the game. '
def checkForDraw():
    for i in board.keys():
        if board[i] == " ":
            return False
        
    return True

' Function to define the restart button of the game. '
def restartGame():
    global game_end
    game_end = False
    for button in buttons:
        button["text"] = " "

    for i in board.keys():
        board[i] = " "

    titleLabel = Label(frame1, text="Tic Tac Toe", font=("Arial", 30), bg = "purple", width=15)
    titleLabel.grid(row=0, column=0)

''' Mini-max algorithm is a recursive or backtracking algorithm which is used in decision-making and game theory.
    It provides an optimal move for the player assuming that opponent is also playing optimally.
    Mini-Max algorithm uses recursion to search through the game-tree. 
    The minimax algorithm performs a depth-first search algorithm for the exploration of the complete game tree. '''
def minimax(board, isMaximizing):
    
    if checkForWin("o"):
        return 1
    
    if checkForWin("x"):
        return -1
    
    if checkForDraw():
        return 0
    
    if isMaximizing:
        bestScore = -100

        for key in board.keys():
            if board[key] == " ":
                board[key] = "o"
                score = minimax(board, False)  # Use of the min-max algorithm.
                board[key] = " "
                
                if score > bestScore:
                    bestScore = score

        return bestScore
    
    else:
        bestScore = 100

        for key in board.keys():
            if board[key] == " ":
                board[key] = "x"
                score = minimax(board, True)  # Use of the min-max algorithm.
                board[key] = " "
                
                if score < bestScore:
                    bestScore = score

        return bestScore

' This function defines how the computer will proceed in single player mode. '
def playComputer():
    bestScore = -100
    bestMove = 0

    for key in board.keys():
        if board[key] == " ":
            board[key] = "o"
            score = minimax(board, False)  # Use of the min-max algorithm.
            board[key] = " "
            
            if score > bestScore:
                bestScore = score
                bestMove = key

    board[bestMove] = "o"

' This is the function which defines how the game is played and all the logical bindings of the game. '
def play(event):
    global turn, game_end
    if game_end:
        return
    button = event.widget
    buttonText = str(button)
    clicked = buttonText[-1]
    
    if clicked == "n":
        clicked = 1
    else:
        clicked = int(clicked)

    if button["text"] == " ":
        if turn == "x":    
            
            board[clicked] = turn
            if checkForWin(turn):
                winningLabel = Label(frame1, text=f"{turn} wins the game", bg="light green", font=("Arial", 26), width=16)
                winningLabel.grid(row=0, column=0, columnspan=3)
                game_end = True
            
            turn = "o"
            updateBoard()

            if mode == "singlePlayer":
                playComputer()
                if checkForWin(turn):
                    winningLabel = Label(frame1, text=f"{turn} wins the game", bg="light green", font=("Arial", 26), width=16)
                    winningLabel.grid(row=0, column=0, columnspan=3)
                    game_end = True
                
                turn = "x"
                updateBoard()

        else:
            
            board[clicked] = turn
            updateBoard()
            if checkForWin(turn):
                winningLabel = Label(frame1, text=f"{turn} wins the game", bg="light green", font=("Arial", 26),  width=16)
                winningLabel.grid(row=0, column=0, columnspan=3)
                game_end = True
            turn = "x"

        if checkForDraw():
            drawLabel = Label(frame1, text=f"Game Draw", bg="Red", font=("Arial", 26), width=16)
            drawLabel.grid(row=0, column=0, columnspan=3)


# ---------------------- UI ----------------------

' Buttons for switching to singleplayer or multiplayer game mode.'

singlePlayerButton = Button(optionFrame, text="Singleplayer", width=13, height=1, font=("Arial", 15), bg="Green", relief=RAISED, borderwidth=5, command=changeModeToSingleplayer)
singlePlayerButton.grid(row=0, column=0, columnspan=1, sticky=NW)

multiPlayerButton = Button(optionFrame, text="Multiplayer", width=13, height=1, font=("Arial", 15), bg="Green", relief=RAISED, borderwidth=5, command=changeModeToMultiplayer)
multiPlayerButton.grid(row=0, column=1, columnspan=1, sticky=NW)

# TIC TAC TOE BOARD

' ROW 1 '
button1 = Button(frame2, text=" ", width=4, height=2, font=("Arial",30), bg="gold", relief=RAISED, borderwidth=5)
button1.grid(row=0, column=0)
button1.bind("<Button-1>",play)

button2 = Button(frame2, text=" ",  width=4, height=2, font=("Arial",30), bg="gold", relief=RAISED, borderwidth=5)
button2.grid(row=0, column=1)
button2.bind("<Button-1>",play)

button3 = Button(frame2, text=" ",  width=4, height=2, font=("Arial",30), bg="gold", relief=RAISED, borderwidth=5)
button3.grid(row=0, column=2)
button3.bind("<Button-1>",play)

' ROW 2 '
button4 = Button(frame2, text=" ",  width=4, height=2, font=("Arial",30), bg="gold", relief=RAISED, borderwidth=5)
button4.grid(row=1, column=0)
button4.bind("<Button-1>",play)

button5 = Button(frame2, text=" ",  width=4, height=2, font=("Arial",30), bg="gold", relief=RAISED, borderwidth=5)
button5.grid(row=1, column=1)
button5.bind("<Button-1>",play)

button6 = Button(frame2, text=" ",  width=4, height=2, font=("Arial",30), bg="gold", relief=RAISED, borderwidth=5)
button6.grid(row=1, column=2)
button6.bind("<Button-1>",play)

' ROW 3 '
button7 = Button(frame2, text=" ",  width=4, height=2, font=("Arial",30), bg="gold", relief=RAISED, borderwidth=5)
button7.grid(row=2, column=0)
button7.bind("<Button-1>",play)

button8 = Button(frame2, text=" ",  width=4, height=2, font=("Arial",30), bg="gold", relief=RAISED, borderwidth=5)
button8.grid(row=2, column=1)
button8.bind("<Button-1>",play)

button9 = Button(frame2, text=" ",  width=4, height=2, font=("Arial",30), bg="gold", relief=RAISED, borderwidth=5)
button9.grid(row=2, column=2)
button9.bind("<Button-1>",play)

' Restart button to replay the game '
restartButton = Button(frame2, text="Restart Game", width=19, height=1, font=("Arial", 20), bg="Grey", relief=RAISED, borderwidth=5, command=restartGame)
restartButton.grid(row=4, column=0, columnspan=3)

' List of all the grid buttons used for tic tac toe game. '
buttons = [button1,button2,button3,button4,button5,button6,button7,button8,button9]

root.mainloop()      # Main loop of the program