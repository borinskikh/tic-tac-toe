import PySimpleGUI as sg

sg.theme('DarkAmber')

array = [
    [' ', '1', '2', '3'],
    ['1', ' ', ' ', ' '],
    ['2', ' ', ' ', ' '],
    ['3', ' ', ' ', ' '],
]

layout = [
    [sg.Text("Player 1's turn\n", key='-TURN-')],
    [sg.Text(array[0][col], key=f'-CELL-0{col}-',
             size=(3, 3)) for col in range(4)],
    [sg.Text(array[1][col], key=f'-CELL-1{col}-',
             size=(3, 3)) for col in range(4)],
    [sg.Text(array[2][col], key=f'-CELL-2{col}-',
             size=(3, 3)) for col in range(4)],
    [sg.Text(array[3][col], key=f'-CELL-3{col}-',
             size=(3, 3)) for col in range(4)],
    [sg.Input(size=(5, 5), key='-INPUT-'), sg.Button('OK', key='-BUTTON-')]
]

window = sg.Window('tic-tac-toe', layout)

playerNumber = 1

playerSymbol = ['', 'x', 'o']

sg.popup('Enter coordinates separated by space to make a move')


def checkForEnd():
    for i in range(1, 4):
        if (array[1][i] == array[2][i] == array[3][i] != ' ' or
            array[i][1] == array[i][2] == array[i][3] != ' ' or
            array[1][1] == array[2][2] == array[3][3] != ' ' or
                array[3][1] == array[2][2] == array[1][3] != ' '):
            return True
    remainingMoves = False
    for i in range(1, 4):
        for j in range(1, 4):
            if array[i][j] == ' ':
                remainingMoves = True
                break
    if not remainingMoves:
        sg.popup('No moves left')
    return False


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    res = [int(i) for i in values['-INPUT-'].split() if i.isdigit()]
    row, col = res[0], res[1]
    if len(res) > 2 or (row > 3 or col > 3) or (row < 1 or col < 1):
        sg.popup('Input is incorrect')
    elif array[row][col] != ' ':
        sg.popup('Cell is occupied')
    else:
        array[row][col] = playerNumber
        cell = '-CELL-' + str(row) + str(col) + '-'
        window[cell].update(playerSymbol[playerNumber])
        if checkForEnd():
            sg.popup('Match is over')
        playerNumber = 2 if playerNumber == 1 else 1
        window['-TURN-'].update("Player " + str(playerNumber) + "'s turn")
    window['-INPUT-'].update('')
window.close()
