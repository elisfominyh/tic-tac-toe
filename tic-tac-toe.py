dict = {}
for i in range(1,10):
    dict[i] = ' '
def check():
    if (dict[1] == dict[2]== dict[3] != ' ' 
    or dict[4] == dict[5]== dict[6] != ' '
    or dict[7] == dict[8]== dict[9] != ' '
    or dict[1] == dict[4]== dict[7] != ' '
    or dict[2] == dict[5]== dict[8] != ' '
    or dict[3] == dict[6]== dict[9] != ' '
    or dict[1] == dict[5]== dict[9] != ' '
    or dict[3] == dict[5]== dict[7] != ' ' ):
        return True

def print_board():
    print(dict[1], '|' , dict[2] , '|', dict[3])
    print('- + - + -') 
    print(dict[4], '|' , dict[5] , '|', dict[6])
    print('- + - + -')
    print(dict[7], '|' , dict[8] , '|', dict[9])
     
def main():

    print('Как хотите сходить?')
    move1 = int(input())
    if dict[move1] == ' ':
        dict[move1] = 'X'
    else:
        print('Нельзя')
    print_board()
    print('Как хотите сходить?')
    move2 = int(input())
    if dict[move2] == ' ':
        dict[move2] = 'O'
    else:
        print('Нельзя')
    print_board()
    if check():
        print('game over')
    else:
        main()
a = input('Хотите сыграть в крестики-нолики?да/нет ')
if a =='да':
    main()
else:
    print('Жаль')

