
def main():
    print("----TIk TAK TOE----")
    print("Welcome to the Game \n")
    p1 = input("Enter name of first player(X):")
    p2 = input("Enter name of second player(O):")
    turn =0
    winner = 'unknown'
    pos = [ '0','1','2','3','4','5','6','7','8']
    def printboard():
        print('Board :')
        print( f'{pos[0]} | {pos[1]} | {pos[2]} ')
        print('---------')
        print( f'{pos[3]} | {pos[4]} | {pos[5]} ')
        print('---------')
        print( f'{pos[6]} | {pos[7]} | {pos[8]} ')
    printboard()
    while(True):
        print("Enter the no of position you wanna mark ,")
        if turn%2 ==0:
            c1 = int(input(f"{p1}'s position : "))
            pos[c1]='X'
            
        else:
            c2 = int(input(f"{p2}'s position : "))
            pos[c2]='O'
        turn+=1
        printboard()
        if pos[0] == pos[1] and pos[1] == pos[2]:
            if pos[0] == 'X':
                winner = p1

            elif pos[0] == 'O':
                winner =p2
        elif pos[3] == pos[4] and pos[4] == pos[5]:
            if pos[3] == 'X':
                winner = p1

            elif pos[3] == 'O':
                winner = p2
        elif pos[6] == pos[7] and pos[7] == pos[8]:
            if pos[6] == 'X':
                winner = p1

            elif pos[6] == 'O':
                winner = p2

        elif pos[0] == pos[3] and pos[3] == pos[6]:
            if pos[0] == 'X':
                winner = p1

            elif pos[0] == 'O':
                winner = p2

        elif pos[1] == pos[4] and pos[4] == pos[7]:
            if pos[1] == 'X':
                winner = p1

            elif pos[1] == 'O':
                winner = p2
        elif pos[2] == pos[5] and pos[5] == pos[8]:
            if pos[2] == 'X':
                winner = p1

            elif pos[2] == 'O':
                winner = p2
        elif pos[0] == pos[4] and pos[4] == pos[8]:
            if pos[0] == 'X':
                winner = p1

            elif pos[0] == 'O':
                winner = p2

        elif pos[6] == pos[4] and pos[4] == pos[2]:
            if pos[6] == 'X':
                winner = p1

            elif pos[6] == 'O':
                winner = p2

        if winner!="unknown":
            break
        i=0
        poscount=0
        for p in pos:
            if p != f'{i}':
                poscount+=1
            i+=1
        if i == poscount :
            print("it's a draw")
            break

    if winner!='unknown':
        print(f'Congratulations !! {winner} won the game.')


if __name__ == '__main__':
    while(True):
        main()
        print("1.Restart 2.Quit")
        choice = int(input("Enter your choice : "))
        if choice == 1:
            print("New Game !!\n")
            continue
        elif choice == 2:
            print("Thanks for playing !")
            break
