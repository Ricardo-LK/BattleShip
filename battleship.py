from os import system, name

ASCII_CODE_a = ord("a")


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

    playerPositionsTable = createTable(tableWidth, tableHeight)
    playerFeedbackTable = createTable(tableWidth, tableHeight)
    computerPositionsTable = createTable(tableWidth, tableHeight)

    playerTakenPositions = []

    for i in range(amountOfShips):
        clearConsole()

        printTable(playerPositionsTable)

        coordsPrompt = f"Digite as coordenadas para o seu navio ({i + 1} de {amountOfShips}) formato: (coluna, linha): "
        coords = getTableCoords(coordsPrompt)

        while True:
            if len(coords) != 2:
                coords = getTableCoords(coordsPrompt)

            elif ord(coords[0]) not in range(ASCII_CODE_a, ASCII_CODE_a + tableWidth) or int(coords[1]) not in range(1, tableHeight + 1):
                print("Esta posição está fora de alcance. Tente novamente")
                coords = getTableCoords(coordsPrompt)

            elif coords in playerTakenPositions:
                print("Esta posição já está preenchida. Tente novamente.")
                coords = getTableCoords(coordsPrompt)
            else:
                playerTakenPositions.append(coords)
                break
        
        tableCoords = [ord(coords[0]) - ASCII_CODE_a, int(coords[1]) - 1]

        playerPositionsTable[tableCoords[1]][tableCoords[0]] = "🚢"
    
    printTable(playerPositionsTable)
        

    
    

def runOriginalMode():
    tableWidth = 10
    tableHeight = 10

    playerPositionsTable = createTable(tableWidth, tableHeight)
    playerFeedbackTable = createTable(tableWidth, tableHeight)
    computerPositionsTable = createTable(tableWidth, tableHeight)






def clearConsole():
    system("cls" if name == "nt" else "clear")

def createTable(width, height):
    table = []
    for row in range(height):
        table.append([])
        for col in range(width):
            table[row].append("🟦")
            
    return table


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

def getTableCoords(prompt):
    coords = input(prompt)
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