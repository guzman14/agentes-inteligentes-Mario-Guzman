import random
import time

class AgenteBuscador:
    def __init__(self, size=5):
        self.size = size
        # Inicializa la matriz (cuadrícula) de tamaño `size x size`
        self.matriz = [["." for _ in range(size)] for _ in range(size)]

        # Posición inicial del agente (esquina superior izquierda)
        self.agente_x, self.agente_y = 0, 0
        self.matriz[self.agente_x][self.agente_y] = "A"

        # Posición aleatoria del objeto
        self.objeto_x, self.objeto_y = random.randint(0, size - 1), random.randint(0, size - 1)
        while (self.objeto_x, self.objeto_y) == (self.agente_x, self.agente_y):
            self.objeto_x, self.objeto_y = random.randint(0, size - 1), random.randint(0, size - 1)
        
        # Coloca el objeto en la cuadrícula
        self.matriz[self.objeto_x][self.objeto_y] = "O"

    def mostrar_matriz(self):
        """Imprime la cuadrícula con la posición del agente (A) y el objeto (O)."""
        for fila in self.matriz:
            print(" ".join(fila))
        print("\n")

    def mover_agente(self):
        """Mueve el agente paso a paso hacia el objeto (A busca a O)."""
        while (self.agente_x, self.agente_y) != (self.objeto_x, self.objeto_y):
            self.matriz[self.agente_x][self.agente_y] = "."  # Borra la posición anterior del agente
            
            # Movimiento hacia el objeto (prioridad en X, luego en Y)
            if self.agente_x < self.objeto_x:
                self.agente_x += 1
            elif self.agente_x > self.objeto_x:
                self.agente_x -= 1
            elif self.agente_y < self.objeto_y:
                self.agente_y += 1
            elif self.agente_y > self.objeto_y:
                self.agente_y -= 1

            self.matriz[self.agente_x][self.agente_y] = "A"  # Actualiza la posición del agente
            self.mostrar_matriz()  # Muestra la cuadrícula con el nuevo movimiento
            time.sleep(1)  # Pausa de 1 segundo para visualizar el movimiento
        
        print("¡El agente encontró el objeto! 🎯")

if __name__ == "__main__":
    agente = AgenteBuscador()  # Crear el agente
    agente.mostrar_matriz()  # Mostrar la cuadrícula inicial
    agente.mover_agente()  # Mover el agente hacia el objeto
