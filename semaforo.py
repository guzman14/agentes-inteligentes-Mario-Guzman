import time
import random

class Semaforo:
    def __init__(self):
        self.estado = "rojo"  # Estado inicial del semáforo
        # Duración base para cada estado (verde, amarillo, rojo)
        self.duracion = {"verde": 5, "amarillo": 2, "rojo": 5}

    def detectar_vehiculos(self):
        """Simula la detección de vehículos (cantidad aleatoria)."""
        return random.randint(0, 20)

    def ajustar_tiempo(self, cantidad_vehiculos):
        """Ajusta la duración del semáforo según la cantidad de vehículos detectados."""
        if cantidad_vehiculos > 10:
            self.duracion["verde"] = 7  # Más tráfico, más tiempo en verde
            self.duracion["rojo"] = 4  # Menos tiempo en rojo
        elif cantidad_vehiculos < 5:
            self.duracion["verde"] = 4  # Menos tráfico, menos tiempo en verde
            self.duracion["rojo"] = 6  # Más tiempo en rojo
        else:
            self.duracion["verde"] = 5  # Estado normal
            self.duracion["rojo"] = 5

    def cambiar_estado(self):
        """Cambia el estado del semáforo cíclicamente y ajusta la duración según la detección de vehículos."""
        while True:
            cantidad_vehiculos = self.detectar_vehiculos()  # Detectar cantidad de vehículos
            self.ajustar_tiempo(cantidad_vehiculos)  # Ajustar tiempos según el tráfico

            # Imprimir el estado actual del semáforo
            print(f"🚦 Estado: {self.estado.upper()} | Vehículos detectados: {cantidad_vehiculos}")
            time.sleep(self.duracion[self.estado])  # Esperar el tiempo según el estado

            # Cambio de estado cíclico
            if self.estado == "verde":
                self.estado = "amarillo"
            elif self.estado == "amarillo":
                self.estado = "rojo"
            else:
                self.estado = "verde"

if __name__ == "__main__":
    semaforo = Semaforo()  # Crear un objeto semáforo
    semaforo.cambiar_estado()  # Iniciar el cambio de estado del semáforo

