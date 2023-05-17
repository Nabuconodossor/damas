class Damas:

    def __init__(self):
        self.tablero = [[" "]*8 for _ in range(8)]
        self.turno = "Blancas"
        self.jugando = True
    
    def mostrar_tablero(self):
        letras = "ABCDEFGH"
        print("   1   2   3   4   5   6   7   8")
        for i in range(8):
            print(letras[i], end=" ")
            for j in range(8):
                print(f"[{self.tablero[i][j]}]", end=" ")
            print()
    
    def mover_pieza(self, origen, destino):
        x1, y1 = origen
        x2, y2 = destino
        pieza = self.tablero[x1][y1]
        
        if pieza == " ":
            print("No hay ninguna pieza en la casilla de origen.")
            return False
        
        if self.tablero[x2][y2] != " ":
            print("La casilla de destino ya está ocupada.")
            return False
        
        # Verificar si el movimiento es válido
        # Aquí debes agregar la lógica para validar el movimiento según las reglas del juego de damas
        
        # Realizar el movimiento
        self.tablero[x1][y1] = " "
        self.tablero[x2][y2] = pieza
        
        # Cambiar el turno
        self.turno = "Blancas" if  self.turno == "Negras"else"Negras"
        
        return True
    
    def jugar(self):

        while self.jugando:

            self.mostrar_tablero()
            print(f"Turno de las {self.turno}")
            origen = input("Ingrese la coordenada de la casilla de origen (por ejemplo, 'A1'): ")
            destino = input("Ingrese la coordenada de la casilla de destino: ")
            
            x1 = ord(origen[0].upper()) - 65
            y1 = int(origen[1]) - 1
            x2 = ord(destino[0].upper()) - 65
            y2 = int(destino[1]) - 1
            
            if not (0 <= x1 < 8) or not (0 <= y1 < 8) or not (0 <= x2 < 8) or not (0 <= y2 < 8):
                print("Coordenadas inválidas.")
                continue
            
            if self.mover_pieza((x1, y1), (x2, y2)):
                print("Movimiento válido.")
            else:
                print("Movimiento inválido. Inténtalo de nuevo.")
        
        print("Fin del juego.")

juego = Damas()
juego.jugar()
