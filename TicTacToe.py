import numpy as np

def main():
    global ttt_array

    ttt_array = np.array(
        ["blank", "blank", "blank"],
        ["blank", "blank", "blank"],
        ["blank", "blank", "blank"],
        ["blank", "blank", "blank"])

    global player_first
    global comp_first

    decision = input(print("Do you want to go first, or do you want the computer to start? If you want to go first, type YES, if not type NO."))

    if decision == "YES":
        player_first = 1 #true
        comp_first = 0

    elif decision == "NO":
        player_first = 0 #false
        comp_first = 1

def ttt_formating():
    ttt_list = []
    #converts the tictactoe_array to board
    secret_ttt = ttt_array.flatten()
    for x in range(0,9):
        if secret_ttt[x] == 0:
            ttt_list.append("0")
        elif secret_ttt[x] == 1:
            ttt_list.append("X")
        elif secret_ttt[x] == "blank":
            ttt_list.append(" ")

def ttt_blanks():
    blanks = []

    blanks_array = (ttt_array == "blank")
    flat_blanks_array = blanks_array.flatten()

    for x in range(0, len(flat_blanks_array)):
        if flat_blanks_array[x] == True:
            blanks.append(x + 1)
    
    return blanks

def end():
    if last_draw == player_first:
        print("You are the winner.")
    elif last_draw == comp_first:
        print("The computer won.")
    elif last_draw == "Draw":
        print("It is a draw. Play again.")

def winner():
    