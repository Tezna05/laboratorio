import time

class Temporizador:
    def __init__(self, duracion):
        self.duracion = duracion 
        self.tiempo_inicial = None
        self.tiempo_restante = duracion
        self.en_ejecucion = False

    def iniciar(self):
        if not self.en_ejecucion:
            self.tiempo_inicial = time.time()  
            self.en_ejecucion = True
            print(f"El temporizador ha comenzado con {self.tiempo_restante} segundos restantes.")
        else:
            print("El temporizador ya está en marcha.")

    def pausar(self):
        if self.en_ejecucion:
            tiempo_transcurrido = time.time() - self.tiempo_inicial
            self.tiempo_restante -= tiempo_transcurrido 
            self.en_ejecucion = False
            print(f"El temporizador ha sido pausado. Tiempo restante: {int(self.tiempo_restante)} segundos.")
        else:
            print("El temporizador no está en marcha.")

    def mostrar_tiempo_restante(self):
        if self.en_ejecucion:
            tiempo_transcurrido = time.time() - self.tiempo_inicial
            tiempo_actual_restante = self.tiempo_restante - tiempo_transcurrido
            print(f"Tiempo restante: {int(tiempo_actual_restante)} segundos.")
        else:
            print(f"Tiempo restante: {int(self.tiempo_restante)} segundos.")

