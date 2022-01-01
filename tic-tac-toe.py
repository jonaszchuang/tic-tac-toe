"""

#Tic Tac Toe Game

"""

grid = [
    ["_", "_", "_"],
    ["_", "_", "_"],
    ["_", "_", "_"]
]

print("")
p1 = str(input("Player one, what is your name? "))
print("")
p2 = str(input("Player two, what is your name? "))
xTurn = True
turns = 0

def board(grid):
    for row in grid:
        for slot in row:
            print(f"{slot} ", end = "")
        print()

def quit(spot):
    if spot == "q":
        return True
    else:
        return False

def check(spot):
    if not isnumb(spot):
        return False
    spot = int(spot)
    if not goodnumb(spot):
        return False
    return True

def isnumb(spot):
    if not spot.isnumeric():
        print("This is not a valid character, ", end = "")
        return False
    else:
        return True

def goodnumb(spot):
    if spot > 9 or spot < 1:
        print("This is not a valid number, ", end = "")
        return False
    else: 
        return True

def taken(coords, grid):
    row = coords[0]
    column = coords[1]
    if grid[row][column] != "_":
        print("This spot is already taken, ", end = "")
        return True
    return False
    
def coordinates(spot):
    row = int(spot / 3)
    column = spot
    if column > 2:
        column = int(column % 3)
    return [row, column]

def add(coords, grid, player):
    row = coords[0]
    column = coords[1]
    grid[row][column] = player

def user(xTurn):
    if xTurn:
        return "X"
    else:
        return "O"

def win(player, grid):
    if rowWin(player, grid):
        return True
    if columnWin(player, grid):
        return True
    if diagonalWin(player, grid):
        return True

def rowWin(player, grid):
    for row in grid:
        completeRow = True
        for slot in row:
            if slot != player:
                completeRow = False
                break
        if completeRow:
            return True
    return False

def columnWin(player, grid):
    for column in range(3):
        completeColumn = True
        for row in range(3):
            if grid[row][column] != player:
                completeColumn = False
                break
        if completeColumn:
            return True
    return False

def diagonalWin(player, grid):
    if (grid[0][0] == player) and (grid[1][1] == player) and (grid[2][2] == player):
        return True
    elif (grid[0][2] == player) and (grid[1][1] == player) and (grid[2][0] == player):
        return True
    else:
        return False

while turns < 9:
    player = user(xTurn)
    board(grid)
    spot = input("Chose a position (1-9) or \"q\" to quit: ")
    if quit(spot):
        break
    if not check(spot):
        print("try again.")
        print("")
        continue
    spot = int(spot) - 1
    coords = coordinates(spot)
    if taken(coords, grid):
        print("try again.")
        continue
    add(coords, grid, player)
    if win(player, grid):
        print("")
        if player == "X":
            print(f"{p1} won! Thanks for playing!")
        else:
            print(f"{p2} won! Thanks for playing!")
        break

    turns += 1
    if turns == 9:
        print("This is a tie. :| Play again for a rematch!")
    xTurn = not xTurn