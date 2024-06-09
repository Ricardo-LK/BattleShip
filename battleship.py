import random
import time
from os import system, name

ASCII_CODE_a = ord("a") # Valor numérico em ASCII da letra 'a'

#RICARDO
EMPTY_VALUE = 0
HAS_SHIP_VALUE = 1
DESTROYED_SHIP_VALUE = 2
MISSED_ATTACK_VALUE = 3

# RENAN
def main():
    clearConsole()
    
    print("                __/___            ")
    print("          _____/______|           ")
    print("  _______/_____\_______\_____     ")
    print("  \              < < <       |    ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    print("*****BATALHA NAVAL*****\n")
    print("Olá! Escolha qual modo de jogo você deseja jogar:")
    print("1 - Modo Simplificado")
    print("2 - Modo Original")

    runSimplifiedMode()

    return 0
    
#RICARDO
def runSimplifiedMode():
    amountOfShips = 5
    
    tableWidth = 10
    tableHeight = 5

    playerShipsPositionsTable = createTable(tableWidth, tableHeight, EMPTY_VALUE)
    computerShipsPositionsTable = createTable(tableWidth, tableHeight, EMPTY_VALUE)

    playerTargetTable = createTable(tableWidth, tableHeight, EMPTY_VALUE)
    computerTargetTable = createTable(tableWidth, tableHeight, EMPTY_VALUE)

    inputPlayerMoves(playerShipsPositionsTable, amountOfShips, tableWidth, tableHeight, HAS_SHIP_VALUE)
    randomizeMoves(computerShipsPositionsTable, amountOfShips, tableWidth, tableHeight, HAS_SHIP_VALUE)

    playerRemainingShips = amountOfShips
    computerRemaininShips = amountOfShips

    hasWinner = False
    winner = "NONE"

    while not hasWinner:
        print("_______________________________________________\n")
        print("***TABULEIRO DO COMPUTADOR***")
        printTable(computerTargetTable, "🟦", "🚢", "💥", "❌")
        print(f"Embarcações restantes: {computerRemaininShips}\n")
        print("_______________________________________________\n")


        print("***TABULEIRO DO JOGADOR***")
        printTable(playerTargetTable, "🟦", "🚢", "💥", "❌")
        print(f"Embarcações restantes: {playerRemainingShips}\n")
        print("_______________________________________________\n")

        playerAttackCoords = inputTableCoords("(JOGADOR) insira a posição para atacar (ex: a, 3): ")
        playerAttackIndexes = tableCoordsToIndexes(playerAttackCoords)

        x = playerAttackIndexes[0]
        y = playerAttackIndexes[1]

        while True:
            if x > tableHeight - 1 or y > tableWidth - 1:
                print("Coordenada fora de alcance. Tente novamente.")

                playerAttackCoords = inputTableCoords("(JOGADOR) insira a posição para atacar (ex: a, 3): ")
                playerAttackIndexes = tableCoordsToIndexes(playerAttackCoords)

                x = playerAttackIndexes[0]
                y = playerAttackIndexes[1]

            elif computerTargetTable[x][y] != EMPTY_VALUE:
                print("Esta coordenada já foi utilizada. Tente novamente.")

                playerAttackCoords = inputTableCoords("(JOGADOR) insira a posição para atacar (ex: a, 3): ")
                playerAttackIndexes = tableCoordsToIndexes(playerAttackCoords)

                x = playerAttackIndexes[0]
                y = playerAttackIndexes[1]
            else:
                break
        
        if computerShipsPositionsTable[x][y] == HAS_SHIP_VALUE:
            computerTargetTable[x][y] = DESTROYED_SHIP_VALUE
            computerRemaininShips -= 1
        elif computerShipsPositionsTable[x][y] == EMPTY_VALUE:
            computerTargetTable[x][y] = MISSED_ATTACK_VALUE

        if computerRemaininShips == 0:
            hasWinner = True
            winner = "PLAYER"
            break

        print("\nO computador está fazendo a sua jogada.", end="", flush=True)

        for _ in range(5):
            print(".", end="", flush=True)
            time.sleep(0.3)
        print()

        x = random.randrange(0, tableHeight)
        y = random.randrange(0, tableWidth)

        while True:
            if playerTargetTable[x][y] != EMPTY_VALUE:
                x = random.randrange(0, tableHeight)
                y = random.randrange(0, tableWidth)
            else:
                break

        if playerShipsPositionsTable[x][y] == HAS_SHIP_VALUE:
            playerTargetTable[x][y] = DESTROYED_SHIP_VALUE
            playerRemainingShips -= 1
        elif playerShipsPositionsTable[x][y] == EMPTY_VALUE:
            playerTargetTable[x][y] = MISSED_ATTACK_VALUE
        
        if playerRemainingShips == 0:
            hasWinner = True
            winner = "COMPUTER"
            break

        clearConsole()
    
    clearConsole()

    for i, row in enumerate(playerTargetTable):
        for j, pos in enumerate(row):
            if playerShipsPositionsTable[i][j] == HAS_SHIP_VALUE and pos != DESTROYED_SHIP_VALUE:
                playerTargetTable[i][j] = HAS_SHIP_VALUE

    for i, row in enumerate(computerTargetTable):
        for j, pos in enumerate(row):
            if computerShipsPositionsTable[i][j] == HAS_SHIP_VALUE and pos != DESTROYED_SHIP_VALUE:
                computerTargetTable[i][j] = HAS_SHIP_VALUE
    
    print("_______________________________________________\n")
    print("***TABULEIRO DO COMPUTADOR***")
    printTable(computerTargetTable, "🟦", "🚢", "💥", "❌")
    print(f"Embarcações restantes: {computerRemaininShips}\n")
    print("_______________________________________________\n")

    
    print("***TABULEIRO DO JOGADOR***")
    printTable(playerTargetTable, "🟦", "🚢", "💥", "❌")
    print(f"Embarcações restantes: {playerRemainingShips}\n")
    print("_______________________________________________\n")

    if winner == "COMPUTER":
        print("FIM DE JOGO! O COMPUTADOR VENCEU!")
    elif winner == "PLAYER":
        print("FIM DE JOGO! O JOGADOR VENCEU!")
    
    print()


#RENAN
# Preenche a tabela do jogador com inputs do usuário.
def inputPlayerMoves(playerPositionsTable, amountOfShips, tableWidth, tableHeight, fill):
    
    # Vetor para armazenar as posições já tomadas.
    playerTakenPositions = []

    # Repete conforme a quantidade de navios determinada
    for i in range(amountOfShips):
        clearConsole()

        printTable(playerPositionsTable, "🟦", fill)

        coordsPrompt = f"Digite as coordenadas para o seu navio ({i + 1} de {amountOfShips}) ex: (a, 3): "
        coords = inputTableCoords(coordsPrompt) # Pega as coordenadas introduzidas pelo usuário
        indexes = tableCoordsToIndexes(coords)
        
        # Continua até que a coordenada seja válida
        while True:

            # Coordenadas já tomadas
            if indexes in playerTakenPositions:
                print("Esta posição já está preenchida. Tente novamente.")
                coords = inputTableCoords(coordsPrompt)
                indexes = tableCoordsToIndexes(coords)
            
            elif indexes[0] > tableHeight - 1 or indexes[0] > tableWidth - 1:
                print("Esta posição está fora de alcance. Tente novamente.")
                coords = inputTableCoords(coordsPrompt)
                indexes = tableCoordsToIndexes(coords)
            
            # Coordenada aceita.
            else:
                playerTakenPositions.append(indexes)
                break

        # Insere a posição
        playerPositionsTable[indexes[0]][indexes[1]] = fill
    
    clearConsole()

#RENAN
# Randomiza as jogadas do computador, preenchendo a sua tabela
def randomizeMoves(computerPositionsTable, amountOfShips, tableWidth, tableHeight, fill):
    
    # Vetor para armazenar as posições já tomadas.
    computerTakenPositions = []

    # Repete conforme a quantidade de navios determinada
    for i in range(amountOfShips):

        # Randomiza as coordenadas
        coords = [random.randint(0, tableHeight - 1), random.randint(0, tableWidth - 1)]

        # Repete até que as coordenadas não sejam repetidas.
        while coords in computerTakenPositions:
            coords = [random.randint(0, tableHeight - 1), random.randint(0, tableWidth - 1)]

        # Adiciona coordenada no vetor de posições tomadas.
        computerTakenPositions.append(coords)

        x = coords[0]
        y = coords[1]

        # Insere navio/caracter na coordenada.
        computerPositionsTable[x][y] = fill

#RENAN
# Limpa o console (compatibilidade entre Windows e Linux)
def clearConsole():
    system("cls" if name == "nt" else "clear")


#RENAN
# Cria uma tabela em forma de matriz, conforme altura,
# largura e caracter de preenchimento
def createTable(width, height, fill):
    table = []
    for row in range(height):
        table.append([])
        for col in range(width):
            table[row].append(fill)
            
    return table


#RENAN
# Imprime uma tabela com as coordenadas a partir de uma matriz
# com formatação.
def printTable(matrix, empty_char, fill_char = "", destroyed_ship_char = "", missed_attack_char = ""):

    # Imprime os indicadores de posição do topo
    print()
    print("    ", end="")
    for i in range(ASCII_CODE_a, ASCII_CODE_a + (len(matrix[0]))):
        print(chr(i), end="  ")
    print()
 
    for i, row in enumerate(matrix):

        # Imprime os indicadores de posição da lateral esquerda
        if len(str(i + 1)) < 2:
            print(f" {i + 1} ", end="")
        else:
            print(f"{i + 1} ", end="")
        
        # Printa o tabuleiro
        for col in row:
            if col == EMPTY_VALUE:
                print(empty_char, end=" ")
            elif col == HAS_SHIP_VALUE:
                print(fill_char, end=" ")
            elif col == DESTROYED_SHIP_VALUE:
                print(destroyed_ship_char, end=" ")
            elif col == MISSED_ATTACK_VALUE:
                print(missed_attack_char, end=" ")

        print()
    
    print()

#RENAN
# Pega coordenadas no formato x, y do usuário de forma
# sanitizada.
def inputTableCoords(prompt):
    coords = input(prompt)
    coords = coords.replace(" ", "")
    coords = coords.split(",")
    coords[0] = coords[0].lower()

    while True:
        # Menos ou mais de dois eixos
        if len(coords) != 2:
            print("Coordenadas inválidas. Tente novamente.")
            coords = input(prompt)
            coords = coords.replace(" ", "")
            coords = coords.split(",")
            coords[0] = coords[0].lower()
            
        # Caracteres inválidos
        elif not (coords[0].isalnum() and coords[1].isnumeric()):
            print("Coordenadas inválidas. Tente novamente.")
            coords = input(prompt)
            coords = coords.replace(" ", "")
            coords = coords.split(",")
            coords[0] = coords[0].lower()

        # Dois caracteres
        elif len(coords[0]) != 1:
            print("Coordenadas inválidas. Tente novamente.")
            coords = input(prompt)
            coords = coords.replace(" ", "")
            coords = coords.split(",")
            coords[0] = coords[0].lower()

        # Coordenada aceita.
        else:
            break

    return coords

#RENAN
# Transforma coordenadas no formato (letra, numero) para índices da matrix
def tableCoordsToIndexes(coords):
    xIndex = int(coords[1]) - 1 # Coordenada x transformada para índice x da matriz
    yIndex = ord(coords[0]) - ASCII_CODE_a # Coordenada y transformada para índice y na matrix

    return [xIndex, yIndex]


#RENAN
# Função para pegar input do usuário de forma segura.
def getInt(prompt):
    while True:
        try:
            integer = int(input(prompt))
            break
        except ValueError:
            pass
    return integer

#RICARDO
main()