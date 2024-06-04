import random
from os import system, name

ASCII_CODE_a = ord("a") # Valor numérico em ASCII da letra 'a'

def main():
    clearConsole()
    
    print("*****BATALHA NAVAL*****")
    print("Olá! Escolha qual modo de jogo você deseja jogar:")
    print("1 - Modo Simplificado")
    print("2 - Modo Original")

    gameMode = 0

    while gameMode not in range(1, 3):
        gameMode = getInt("Modo: ")

    if gameMode == 1:

        runSimplifiedMode()

    elif gameMode == 2:

        runOriginalMode()
    

def runSimplifiedMode():
    amountOfShips = 5
    tableWidth = 10
    tableHeight = 5

    playerPositionsTable = createTable(tableWidth, tableHeight, "🟦")
    playerFeedbackTable = createTable(tableWidth, tableHeight, "🟦")
    computerPositionsTable = createTable(tableWidth, tableHeight, "🟦")

    inputPlayerMoves(playerPositionsTable, amountOfShips, "🚢", tableWidth, tableHeight)


    randomizeMoves(computerPositionsTable, amountOfShips, tableWidth, tableHeight, "🚢")
    playerAttackTakenPositions = []

    while True:
        playerAttack(playerAttackTakenPositions, playerFeedbackTable, tableWidth, tableHeight)
        computerAttack()
    printTable(playerPositionsTable)

# Preenche a tabela do jogador com inputs do usuário.
def inputPlayerMoves(playerPositionsTable, amountOfShips, fillChar, tableWidth, tableHeight):
    
    # Vetor para armazenar as posições já tomadas.
    playerTakenPositions = []

    # Repete conforme a quantidade de navios determinada
    for i in range(amountOfShips):
        clearConsole()

        printTable(playerPositionsTable)

        coordsPrompt = f"Digite as coordenadas para o seu navio ({i + 1} de {amountOfShips}) formato: (coluna, linha): "
        coords = getTableCoords(coordsPrompt) # Pega as coordenadas introduzidas pelo usuário
        
        # Continua até que o input do usuário seja válido
        coords = validateUserInput(coords, coordsPrompt, playerTakenPositions, tableWidth, tableHeight)
        
        xCoord = int(coords[1]) - 1 # Coordenada x transformada para índice x da matriz
        yCoord = ord(coords[0]) - ASCII_CODE_a # Coordenada y transformada para índice y na matrix

        # Insere na posição o navio/caracter
        playerPositionsTable[xCoord][yCoord] = fillChar
    
    clearConsole()

# Randomiza as jogadas do computador, preenchendo a sua tabela com 
def randomizeMoves(computerPositionsTable, amountOfShips, tableWidth, tableHeight, fillChar):
    
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
        computerPositionsTable[x][y] = fillChar


def runOriginalMode():
    tableWidth = 10
    tableHeight = 10

    playerPositionsTable = createTable(tableWidth, tableHeight)
    playerFeedbackTable = createTable(tableWidth, tableHeight)
    computerPositionsTable = createTable(tableWidth, tableHeight)


def playerAttack(playerAttackTakenPositions, playerFeedbackTable, tableWidth, tableHeight):

    attackCoordsPrompt = f"Digite as coordenadas para o seu ataque. formato: (coluna, linha): "
    attackCoords = getTableCoords(attackCoordsPrompt)

    attackCoords = validateUserInput(attackCoords, attackCoordsPrompt, playerAttackTakenPositions, tableWidth, tableHeight)
    playerAttackTakenPositions.append(attackCoords)

    xCoord = int(attackCoords[1]) - 1 # Coordenada x transformada para índice x da matriz
    yCoord = ord(attackCoords[0]) - ASCII_CODE_a # Coordenada y transformada para índice y na matrix

    playerFeedbackTable[xCoord][yCoord] = "💥"

def computerAttack():
    pass

def validateUserInput(coords, coordsPrompt, playerTakenPositions, tableWidth, tableHeight):
    while True:
            
        # Menos de 2 eixos nas coordenadas
        if len(coords) != 2:
            print("Coordenadas inválidas. Tente novamente.")
            coords = getTableCoords(coordsPrompt)
        
        # Caracteres inválidos
        elif not (coords[0].isalnum() and coords[1].isnumeric()):
            print("Coordenadas inválidas. Tente novamente.")
            coords = getTableCoords(coordsPrompt)

        # Coordenadas fora dos limites
        elif ord(coords[0]) not in range(ASCII_CODE_a, ASCII_CODE_a + tableWidth) or int(coords[1]) not in range(1, tableHeight + 1):
            print("Esta posição está fora de alcance. Tente novamente.")
            coords = getTableCoords(coordsPrompt)

        # Coordenadas já tomadas
        elif coords in playerTakenPositions:
            print("Esta posição já está preenchida. Tente novamente.")
            coords = getTableCoords(coordsPrompt)
        
        # Coordenada aceita.
        else:
            playerTakenPositions.append(coords)
            break

    return coords

# Limpa o console (compatibilidade entre Windows e Linux)
def clearConsole():
    system("cls" if name == "nt" else "clear")


# Cria uma tabela em forma de matriz, conforme altura,
# largura e caracter de preenchimento
def createTable(width, height, fillChar):
    table = []
    for row in range(height):
        table.append([])
        for col in range(width):
            table[row].append(fillChar)
            
    return table


# Imprime uma tabela com as coordenadas a partir de uma matriz
# com formatação.
def printTable(matrix):
    print()
    print("    ", end="")
    for i in range(ASCII_CODE_a, ASCII_CODE_a + (len(matrix[0]))):
        print(chr(i), end="  ")
    print()
 
    for i, row in enumerate(matrix):
        if len(str(i + 1)) < 2:
            print(f" {i + 1} ", end="")
        else:
            print(f"{i + 1} ", end="")
        
        for col in row:
            print(col, end=" ")
        print()
    
    print()

# Pega coordenadas no formato x, y do usuário de forma
# sanitizada.
def getTableCoords(prompt):
    coords = input(prompt)
    coords = coords.replace(" ", "")
    coords = coords.split(",")
    coords[0] = coords[0].lower()

    return coords


# Função para pegar input do usuário de forma segura.
def getInt(prompt):
    while True:
        try:
            integer = int(input(prompt))
            break
        except ValueError:
            pass
    return integer

main()