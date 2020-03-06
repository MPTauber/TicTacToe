import numpy as np

def main():
    global ttt_array

    ttt_array = np.array(
        ["blank", "blank", "blank"],
        ["blank", "blank", "blank"],
        ["blank", "blank", "blank"],
        ["blank", "blank", "blank"])
    
    tutorial_arr = np.array(
        [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]])

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

def end(last_draw):
    if last_draw == player_first:
        print("You are the winner.")
    elif last_draw == comp_first:
        print("The computer won.")
    elif last_draw == "Draw":
        print("It is a draw. Play again.")

def winner(last_draw):
    if ttt_blanks == []:
        end("It is a draw. Play again.")
    
    for x in range(0,3):
        rows_win = (ttt_array[x, :] == last_draw).all()
        cols_win = (ttt_array[:, x] == last_draw).all()

    diag1_win = (np.diag(ttt_array) == last_draw).all()
    diag2_win = (np.diag(np.fliplr(ttt_array)) == last_draw).all()
    
    if diag1_win or diag2_win:
        end(last_draw)

        next_turn(last_draw)

def next_turn(last_draw):
    if last_draw == player_first:
        comp_turn()
    elif last_draw == comp_first:
        user_turn()


def place_mark(current_num, current_input):
    index = np.where(tutorial_arr == current_input)
    ttt_array[index] = current_num


def user_turn():
    display_board()
    
    user_input = input("Pick an open slot: ")
    user_input = int(user_input)
    
    if user_input in return_open_slots():
        place_letter(user_num, user_input)
    else:
        print("That's not a open slots.")
        user_turn()
        
    check_for_winner(user_num)
    

def comp_turn():
# Randomly chooses from open_slots to place its letter    
    open_slots = return_open_slots()
    comp_input = random.choice(open_slots)
    place_letter(comp_num, comp_input)
    check_for_winner(comp_num)
    

main()