
from tkinter import Tk, Canvas, Frame, Button, LEFT, RIGHT, messagebox, CURRENT
from random import *


def clicks(event):
    if canvas.find_withtag(CURRENT):
        global last_piece, piece_name

        piece_name = canvas.gettags(CURRENT)[0]
        group_name = piece_name[0]
        if pieces == [12]:
            last_piece = None

        try:
            if piece_name == "AI_first":
                AI_to_play()
            elif group_name != last_piece and last_piece != None and piece_name != 'DONE':
                # display ILLEGAL MOVE in the game canvas for 1.5 seconds if the user tries to pick pieces from different piles on the same turn
                canvas.create_text(355, 40, text="ILLEGAL MOVE", font="Purisa", tags="ILLEGAL_WARNING", fill="black",command=None)
                canvas.update_idletasks()
                canvas.after(1500)
                canvas.delete("ILLEGAL_WARNING")
            else:
                if piece_name == 'DONE' and last_piece != 'DONE' and last_piece != None:
                    last_piece = None
                    AI_to_play() # this is for the computer's turn when the user has clicked the Done button
                elif piece_name == 'DONE' and last_piece == None:
                    # do not let the user click the done button more than once in a row. Displays the message for 1.5 seconds
                    canvas.create_text(355, 40, text="YOU HAVE NOT MADE ANY MOVES", font="Purisa", tags="DOUBLE_DONE",fill="black", command=None)
                    canvas.update_idletasks()
                    canvas.after(1500)
                    canvas.delete("DOUBLE_DONE")
                elif piece_name == 'WON_BUTTON':
                    pass
                else:
                    canvas.delete('AI_first')
                    update_board(piece_name)
                    canvas.delete(piece_name)
                    last_piece = piece_name[0]
                    if sum(pieces) == 0:
                        game_over('computer')
        except NameError:
            last_piece = group_name
            if piece_name == 'DONE':
                AI_to_play()  # this is the computer's turn when the user has clicked the Done button
            elif piece_name == 'WON_BUTTON':
                pass
            else:
                update_board(piece_name)
                canvas.delete(piece_name)
                # this should only happen on first go and is to catch the case where the last button press is not defined
                last_piece = piece_name[0]
                if sum(pieces) == 0:
                    game_over('computer')

def create_pieces():

    # ititialise the mathematical representations of the board and declare as global variable so it can easily be updated within the update function
    global pieces, board, piece_name
    pieces = [12]
    board = [[1,1,1,1,1,1,1,1,1,1,1,1]]
    piece_name = 'NEW_GAME'

    circle_size = 40
    linecolour = "violet"
    fillcolour = "violet"

    # Group A is on the left. It is a group of 7

    A1x = 50
    A1y = 160
    
    A2x = 110
    A2y = 160
    
    A3x = 170
    A3y = 160
    
    A4x = 230
    A4y = 160
    
    A5x = 290
    A5y = 160
    
    A6x = 350
    A6y = 160
    
    A7x = 410
    A7y = 160
    
    A8x = 470
    A8y = 160
    
    A9x = 530
    A9y = 160
    
    A10x = 590
    A10y = 160
    
    A11x = 650
    A11y = 160
    
    A12x = 710
    A12y = 160
    
    canvas.create_rectangle(A1x, A1y, A1x+circle_size, A1y+circle_size, outline=linecolour,fill=fillcolour,tags="A1")
    canvas.create_rectangle(A2x, A2y, A2x+circle_size, A2y+circle_size, outline=linecolour,fill=fillcolour,tags="A2")
    canvas.create_rectangle(A3x, A3y, A3x+circle_size, A3y+circle_size, outline=linecolour,fill=fillcolour,tags="A3")
    canvas.create_rectangle(A4x, A4y, A4x+circle_size, A4y+circle_size, outline=linecolour,fill=fillcolour,tags="A4")
    
    canvas.create_rectangle(A5x, A5y, A5x+circle_size, A5y+circle_size, outline=linecolour,fill=fillcolour,tags="A5")
    canvas.create_rectangle(A6x, A6y, A6x+circle_size, A6y+circle_size, outline=linecolour,fill=fillcolour,tags="A6")
    canvas.create_rectangle(A7x, A7y, A7x+circle_size, A7y+circle_size, outline=linecolour,fill=fillcolour,tags="A7")
    canvas.create_rectangle(A8x, A8y, A8x+circle_size, A8y+circle_size, outline=linecolour,fill=fillcolour,tags="A8")
    
    canvas.create_rectangle(A9x, A9y, A9x+circle_size, A9y+circle_size, outline=linecolour,fill=fillcolour,tags="A9")
    canvas.create_rectangle(A10x, A10y, A10x+circle_size, A10y+circle_size, outline=linecolour,fill=fillcolour,tags="A10")
    canvas.create_rectangle(A11x, A11y, A11x+circle_size, A11y+circle_size, outline=linecolour,fill=fillcolour,tags="A11")
    canvas.create_rectangle(A12x, A12y, A12x+circle_size, A12y+circle_size, outline=linecolour,fill=fillcolour,tags="A12")

    print(type(board))
    print(board)

def create_DONE_button():
    canvas.create_rectangle(570,2,680,45,outline="white",fill="violet",tags="DONE")
    canvas.create_text(630,23,text="AI turn",font="Purisa",tags="DONE")

def create_computer_go_first_button():
    canvas.create_rectangle(570,48,680,91,outline="white",fill="violet",tags="AI_first")
    canvas.create_text(630,70,text="AI go first",font="Purisa",tags="AI_first")


def operation_buttons():
    # create the buttons to start the game and show the rules
    operation_frame = Frame()
    operation_frame.pack(fill="both", expand=True)
    Start = Button(operation_frame, text='START', height=3, command=start_game, bg='black',fg='violet')
    Start.pack(fill="both", expand=True, side=LEFT)
    Rules = Button(operation_frame, text='GAME RULES', command=game_rules, height=3, bg='black',fg='violet')
    Rules.pack(fill="both", expand=True, side=RIGHT)
    
def start_game():
    create_pieces()
    create_DONE_button()
    create_computer_go_first_button()
    canvas.delete('WON_BUTTON')
    canvas.bind("<Button-1>",func=clicks)

def game_rules():
    rules = 'Welcome to Nim.\n'
    message_of_rules = rules
    messagebox.showinfo("Nim Game", message_of_rules)

def update_board(piece_names):
    if type(piece_names) == str:    #need to tell if there is a single or multiple updates to be done
        update_board_pieces(piece_names)
    else:
        for item in range(0, len(piece_names)): # multiple updates are required when the AI makes its moves
            piece_name = piece_names[item]
            update_board_pieces(piece_name)

def update_board_pieces(piece_name):

    group_name = piece_name[0]
    if group_name == 'A':
        pieces[0] -= 1

    if piece_name == 'A1':
        board[0][0] = 0
    elif piece_name == 'A2':
        board[0][1] = 0
    elif piece_name == 'A3':
        board[0][2] = 0
    elif piece_name == 'A4':
        board[0][3] = 0
    elif piece_name == 'A5':
        board[0][4] = 0
    elif piece_name == 'A6':
        board[0][5] = 0
    elif piece_name == 'A7':
        board[0][6] = 0
    elif piece_name == 'A8':
        board[0][7] = 0
    elif piece_name == 'A9':
        board[0][8] = 0
    elif piece_name == 'A10':
        board[0][9] = 0
    elif piece_name == 'A11':
        board[0][10] = 0
    elif piece_name == 'A12':
        board[0][11] = 0

    # piece_index = int(piece_name[1:])
    # board[0][piece_index] = 0

def AI_to_play():
    # this finds the computer's action using the strategies defined
    delta = find_next_position()
    canvas.delete("AI_first")

    # this applies the strategy and consist of the computer building a list of board moves it must make to apply the strategy has determined is best
    if finish == False:
        # delta is the difference is the current state and the future state of the board
        # delta should only every have 1 number of the 3 that is greater than zero. eg. [0,3,0] tells the program to remove 3 pieced from pile B
        # delta = [pieces[0] - next_position[0], pieces[1] - next_position[1], pieces[2] - next_position[2]]
        pieces_to_take = []

        if delta > 0:
            # take from A
            piece_index = 0
            number_of_pieces_to_take = delta
            while number_of_pieces_to_take > 0:
                if board[0][piece_index] == 1:
                    board[0][piece_index] = 0
                    pieces[0] -= 1
                    piece_index += 1
                    number_of_pieces_to_take -= 1
                    pieces_to_take.append('A' + str(piece_index))
                else:
                    piece_index += 1

    # this is the computer actually making the moves iteratively for each move it has decided
    if finish == False:
        for piece in pieces_to_take:
            canvas.itemconfig(piece, fill="white") # change the colour of the pieces the AI selects to yellow before deleting them
            canvas.update_idletasks()
            canvas.after(500) #500ms delay to allow the user to see the pieces change colour before the AI deletes them
            canvas.delete(piece) # delete each piece the AI selects
            if sum(pieces) == 0: #check if the user has won
                game_over(player)

def game_over(who_won):  # displays the final message of who won

    button_width = 190
    button_height = 40
    BX = 260
    BY = 110
    canvas.delete('DONE')
    canvas.create_rectangle(BX, BY, BX + button_width, BY + button_height, outline="black", fill="white",
                            tags="WON_BUTTON", command=None)
    if who_won == 'user':
        canvas.create_text(BX + 95, BY + 20, text="!!! YOU WON !!!", font="Purisa", tags="WON_BUTTON",
                           fill="violet", command=None)
    elif who_won == 'computer':
        canvas.create_text(BX + 95, BY + 20, text="AI WON", font="Purisa", tags="WON_BUTTON",
                           fill="violet", command=None)



from nim_player import *
from nim_game import *

def find_next_position():
    global finish
    finish = False
    print(pieces)
    game = Nim(pieces[0]+1)
    AI_Player = AI('PC')
    delta = AI_Player.choose_move(game)
    print(f'AI played {delta}')
    if pieces == [0]:
        finish = True
    # delta = drop_stones(pieces)

    return delta

#this is the main program
root = Tk()
root.title('Nim Game')
canvas = Canvas(root, bg = "black",width=800, height=300)
canvas.pack()
