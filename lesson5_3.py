# Создайте программу для игры в ""Крестики-нолики""

from tkinter import *

def push(x):
    global game
    global game_left
    global turn
    if turn == 0:
        game[x] = 'X'
        buttons[x].config(text = 'X', bg = 'grey', state = 'disabled')
        game_left.remove(x)
        turn += 1
        label['text'] = f'Ваш ход, {player_2}'
    else:
        game[x] = "O"
        buttons[x].config(text = 'O', bg = 'grey', state = 'disabled')
        game_left.remove(x)
        turn -= 1
        label['text'] = f'Ваш ход, {player_1}'

    if game[0] == 'X' and game[1] == 'X' and game[2] == 'X' or game[3] == 'X' and game[4] == 'X' and game[5] == 'X' or game[6] == 'X' and game[7] == 'X' and game[8] == 'X' or \
    game[0] == 'X' and game[3] == 'X' and game[6] == 'X' or game[1] == 'X' and game[4] == 'X' and game[7] == 'X' or game[2] == 'X' and game[5] == 'X' and game[8] == 'X' or \
    game[0] == 'X' and game[4] == 'X' and game[8] == 'X' or game[2] == 'X' and game[4] == 'X' and game[6] == 'X':
        label['text'] = f'{player_1}, вы победили!'
        for i in game_left:
            buttons[i].config(state = 'disabled')
    elif game[0] == 'O' and game[1] == 'O' and game[2] == 'O' or game[3] == 'O' and game[4] == 'O' and game[5] == 'O' or game[6] == 'O' and game[7] == 'O' and game[8] == 'O' or \
    game[0] == 'O' and game[3] == 'O' and game[6] == 'O' or game[1] == 'O' and game[4] == 'O' and game[7] == 'O' or game[2] == 'O' and game[5] == 'O' and game[8] == 'O' or \
    game[0] == 'O' and game[4] == 'O' and game[8] == 'O' or game[2] == 'O' and game[4] == 'O' and game[6] == 'O':
        label['text'] = f'{player_2}, вы победили!'
        for i in game_left:
            buttons[i].config(state = 'disabled')
    elif len(game_left) < 1:
        label['text'] = 'Игра окончена!'
        
game = [None] * 9
game_left = list(range(9))
turn = 0
player_1 = input('Введите имя первого игрока: ')
player_2 = input('Введите имя второго игрока: ')
win = Tk()
win.title('Крестики-нолики')
win.config(bg='gray')

label = Label(win, width=30, text=f'Игра началась!\nВаш ход, {player_1}',font=('Arial', 20, 'bold'), bg='gray')

buttons = [Button(win, width=5, height=3, font=('Arial', 28, 'bold'), bg='blue', activebackground = 'green', command = lambda x=i: push(x)) for i in range(9)]
row = 1
col = 0
for i in range(9):
    buttons[i].grid(row=row, column=col)
    col += 1
    if col == 3:
        row += 1
        col = 0

label.grid(row=0,column=0,columnspan=3)
win.mainloop()
