import random

win = False
lifes = 3
difficulty = 0

camp_size_veryeasy = 4
camp_size_easy = 8
camp_size_medium = 16
camp_size_hard = 32

bombs_veryeasy = 3
bombs_easy = 10
bombs_medium = 40
bombs_hard = 160

camp = [0]

# bombs = -1
# empty = 0
# numbers = 1, 2, 3, 4, 5, 6, 7, 8

def ChooseDifficulty ():
    while difficulty == 0:
        print ("1 = Very Easy  //  2 = Easy  //  3 = Medium  // 4 = Hard")
        chosen_difficulty = int(input("Input Difficulty: "))
        if chosen_difficulty == 1:

            camp = [0] * camp_size_veryeasy
            for i in range(camp_size_veryeasy):
                camp[i] = [0] * camp_size_veryeasy
                for j in range (camp_size_veryeasy):
                    camp[i][j] = [0] *2
                    camp[i][j][0] = 0
                    camp[i][j][1] = False
            PutBombs(camp, bombs_veryeasy)
            CalculateNumbers(camp)
            return hidden_camp

        elif chosen_difficulty == 2:
            camp = [0] * camp_size_easy
            for x in range(camp_size_easy):
                camp[x] = [0, 0] * camp_size_easy
            PutBombs(camp, bombs_easy)
            CalculateNumbers(camp)
            return hidden_camp

        elif chosen_difficulty == 3:
            camp = [0] * camp_size_medium
            for x in range(camp_size_medium):
                camp[x] = [0, 0] * camp_size_medium
            PutBombs(camp, bombs_medium)
            CalculateNumbers(camp)
            return hidden_camp

        elif chosen_difficulty == 4:
            camp = [0] * camp_size_hard
            for x in range(camp_size_hard):
                camp[x] = [0, 0] * camp_size_hard
            PutBombs(camp, bombs_hard)
            CalculateNumbers(camp)
            return hidden_camp

        else:
            print("Please input correct number")


def PutBombs (camp, number_of_bombs):
    number_of_placed_bombs = 0
    while number_of_placed_bombs < number_of_bombs:
        bombX = random.randint(0, len(camp)-1)
        bombY = random.randint(0, len(camp)-1)
        if camp[bombX][bombY][0] == 0:
            camp[bombX][bombY][0] = -1
            number_of_placed_bombs += 1


def CalculateNumbers(camp):
    for y in range (len(camp)):
        for x in range (len(camp[y])):
            if camp[x][y][0] == 0:
                number_of_bombs = 0
                for j in range (-1, 2):
                    for k in range (-1, 2):
                        if -1 < x+k < len(camp) and -1 < y+j < len(camp):
                            if camp[x+k][y+j][0] == -1:
                                number_of_bombs += 1

                camp[x][y][0] = number_of_bombs
    return camp


def PrintCamp (camp):
    for i in range(len(camp)):
        for j in range (len(camp[i])):
            if camp[i][j][1] is True:
                if hidden_camp[i][j][0] == -1:
                    print("B", end=" ")
                elif hidden_camp[i][j][0] == 0:
                    print("0", end=" ")
                else:
                    print(hidden_camp[i][j][0], end=" ")
            elif camp[i][j][1] is False:
                print("-", end=" ")
        print("")
    print("")

def PrintHidden (camp):
    print ("This is the hidden camp:")
    for i in range(0, len(camp), 1):
        for j in range (0, len(camp[i]), 1):
            if camp[i][j][0] == -1:
                print ("B", end=" ")
            elif camp[i][j][0] == 0:
                print ("-", end=" ")
            else:
                print(camp[i][j][0], end=" ")
        print("")
    print("")



#while win is False and lifes > 0:

hidden_camp = ChooseDifficulty()
PrintHidden(hidden_camp)
PrintCamp(camp)


#PrintCamp(camp)
