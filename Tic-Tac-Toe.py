# write your code here
import time
print("Co-ordinate vise tic-tac-toe".title())
print("enter 9 spaces to start the game".title())
print()
a = input("Enter cells: ")
c = 0
c1 = 0
di = {"b13" : a[0], "b23" : a[1], "b33" : a[2],
      "b12" : a[3], "b22" : a[4], "b32" : a[5],
      "b11" : a[6], "b21" : a[7], "b31" : a[8]}
for i in a:
    if i == "X":
        c += 1
    elif i == "O":
        c1 += 1  
total = c + c1
def C(*l):
    for i in range(1,4):
        global c
        global c1
        for j in range(1, 4):
            if l[0] == i and l[1] == j:
                if c > c1:
                    di["b" + str(i) + str(j)] = "O"
                    c1 += 1
                else:
                    di["b" + str(i) + str(j)] = "X"
                    c += 1                
def D():
    for i in range(1, 4):
        for j in range(1, 2):
            if di["b" + str(i) + str(j)] == di["b" + str(i) + str(j + 1)] == di["b" + str(i) + str(j + 2)] == "X":
                return 1
            elif di["b" + str(i) + str(j)] == di["b" + str(i) + str(j + 1)] == di["b" + str(i) + str(j + 2)] == "O":
                return 2
            elif di["b" + str(j) + str(i)] == di["b" + str(j + 1) + str(i)] == di["b" + str(j + 2) + str(i)] == "X":
                return 1
            elif di["b" + str(j) + str(i)] == di["b" + str(j + 1) + str(i)] == di["b" + str(j + 2) + str(i)] == "O":
                return 2
    if di["b11"] == di["b22"] == di["b33"] == "X":
        return 1
    elif di["b11"] == di["b22"] == di["b33"] == "O":
        return 2
    elif di["b13"] == di["b22"] == di["b31"] == "X":
        return 1
    elif di["b13"] == di["b22"] == di["b31"] =="O":
        return 2
    else:
        return 3
print("  ---------")
print(f"| 13 23 33 |")
print(f"| 12 22 32 |")
print(f"| 11 21 31 |")
print("  ---------")
while True:
    try:
        if c <= c1:
            B = list(map(int, input("Player 1 enter the coordinates: ").split()))
        else:
            B = list(map(int, input("Player 2 enter the coordinates: ").split()))
    except ValueError:
        print("You should enter numbers!")
    else:
        if B[0] > 3 or B[1] > 3:
            print("Coordinates should be from 1 to 3! with a space between them")
            continue
        elif di["b" + str(B[0]) + str(B[1])] == "X" or di["b" + str(B[0]) + str(B[1])] == "O":
            print("This cell is occupied! Choose another one!")
            continue
        else:    
            C(*B)
            print("---------")
            print(f"| {di['b13']} {di['b23']} {di['b33']} |")
            print(f"| {di['b12']} {di['b22']} {di['b32']} |")
            print(f"| {di['b11']} {di['b21']} {di['b31']} |")
            print("---------")
        if D() == 1:
            print("PLAYER 1 WINS")
            break
        elif D() == 2:
            print("PLAYER 2 WINS")
            break
        else:
            total += 1
        if total == 9:
            print("DRAW")
            break
        elif total != 9:
            print("Game not finished")
time.sleep(5)
