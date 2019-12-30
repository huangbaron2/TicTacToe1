matrix = [["-", "-" , "-" ],
          ["-", "-" , "-" ],
          ["-", "-" , "-" ]]
player = 0 
counter = 0

print("Player 1 is O")
print("Player 2 is X")
for rows in matrix:
    print(rows)
print('\n')

def ask_player():
    global counter
    if  player == 0:
        print("Player 1's Turn")
    else:
        print("Player 2's Turn")
    counter += 1
        
def game_play_logic():
    global player
    state = 3
    while state == 3:
        ask_player()
        coord = pick_a_number()
        draw_matrix(coord)
        state = check_win()
    if state == 1:
        print('Player 2 Wins')
        quit()
    if state == 2:
        print('player 1 Wins')
        quit()
    
        
    
def pick_a_number():
    labels = {1:(0,0), 2:(0,1), 3:(0,2), 4:(1,0), 5:(1,1), 6:(1,2), 7:(2,0), 8:(2,1), 9:(2,2)}
    print('Pick a number between 1 and 9')
    try:
        player_input = input()
        if player_input == "board":
            for row in matrix:
                print(row)
        if int(player_input) not in (range(1, 10)):
            print('Invalid coordinate')
            game_play_logic()
        coord = labels[int(player_input)]
        return coord
    except:
        print('Cannot enter nothing')
        game_play_logic()

def draw_matrix(coord):
    global player
    while matrix[coord[0]][coord[1]] == "X" or matrix[coord[0]][coord[1]] == "O":
        print('Coordinate Taken')
        game_play_logic()
    if player == 0:
        if matrix[coord[0]][coord[1]] == "-":
            matrix[coord[0]][coord[1]] = "X"
    else:
        if matrix[coord[0]][coord[1]] == "-":
            matrix[coord[0]][coord[1]] = "O"
    for row in matrix:
        print(row)

def check_win():
    global counter
    global player
    for row in matrix:
        if len(set(row)) == 1:
            if row[0] == "O":
                return 1
            if row[0] == "X":
                return 2
            
    if len(set(matrix[i][0] for i in range(len(matrix)))) == 1:
        if matrix[0][0] == "O":
            return 1
        if matrix[0][0] == "X":
            return 2
    if len(set(matrix[i][1] for i in range(len(matrix)))) == 1:
        if matrix[0][1] == "O":
            return 1
        if matrix[0][1] == "X":
            return 2
    if len(set(matrix[i][2] for i in range(len(matrix)))) == 1:
        if matrix[0][2] == "O":
            return 1
        if matrix[0][2] == "X":
            return 2
        
    if len(set([matrix[i][i] for i in range(len(matrix))])) == 1:
        if matrix[0][0] == "O":
            return 1
        if matrix[0][0] == "X":
            return 2
        
    if len(set(matrix[i][len(matrix)-i-3] for i in range(len(matrix)))) == 1:
        if matrix[0][2] == "O":
            return 1
        if matrix[0][2] == "X":     
            return 2
    '''   
    if "-" not in matrix[0]:
        if "-" not in matrix[1]:
            if "-" not in matrix[2]:
                print('Tie')
                end()
    '''
    if counter == 9:
        print('Tie')
        end()
    if player == 0:
        player += 1
    else:
        player -= 1
    
    return 3

def end():
    exit()

game_play_logic()
