# Definición del tablero
tablero = [
    ["[ ]", "[○]", "[ ]", "[○]", "[ ]", "[○]", "[ ]", "[○]"],
    ["[○]", "[ ]", "[○]", "[ ]", "[○]", "[ ]", "[○]", "[ ]"],
    ["[ ]", "[○]", "[ ]", "[○]", "[ ]", "[○]", "[ ]", "[○]"],
    ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
    ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
    ["[●]", "[ ]", "[●]", "[ ]", "[●]", "[ ]", "[●]", "[ ]"],
    ["[ ]", "[●]", "[ ]", "[●]", "[ ]", "[●]", "[ ]", "[●]"],
    ["[●]", "[ ]", "[●]", "[ ]", "[●]", "[ ]", "[●]", "[ ]"]
]

# Función para imprimir el tablero
def imprimir_tablero():
    print("     0    1    2    3    4    5    6    7")
    print("  ┌────────────────────────────────────────┐")
    for i, fila in enumerate(tablero):
        print(f"{i} │ {'  '.join(fila)} │")
    print("  └────────────────────────────────────────┘")

# Función para realizar un movimiento
def realizar_movimiento(fila_actual, columna_actual, fila_destino, columna_destino):
    # Verificar límites del tablero
    if fila_actual < 0 or fila_actual >= len(tablero) or columna_actual < 0 or columna_actual >= len(tablero[0]):
        print("La posición actual está fuera del tablero.")
        return
    if fila_destino < 0 or fila_destino >= len(tablero) or columna_destino < 0 or columna_destino >= len(tablero[0]):
        print("La posición destino está fuera del tablero.")
        return

    # Verificar si la posición actual contiene una ficha
    ficha_actual = tablero[fila_actual][columna_actual]
    if ficha_actual == "[ ]":
        print("No hay una ficha en la posición actual.")
        return

    # Verificar si la posición destino está vacía
    if tablero[fila_destino][columna_destino] != "[ ]":
        print("La posición destino está ocupada.")
        return

    # Realizar el movimiento
    tablero[fila_actual][columna_actual] = "[ ]"
    tablero[fila_destino][columna_destino] = ficha_actual

    # Imprimir el tablero después del movimiento
    imprimir_tablero()

# Ejemplo de uso
imprimir_tablero()
print("")

fila_actual = int(input("Ingrese la fila de la ficha que desea mover: "))
columna_actual = int(input("Ingrese la columna de la ficha que desea mover: "))
fila_destino = int(input("Ingrese la fila destino: "))
columna_destino = int(input("Ingrese la columna destino: "))

realizar_movimiento(fila_actual, columna_actual, fila_destino, columna_destino)
