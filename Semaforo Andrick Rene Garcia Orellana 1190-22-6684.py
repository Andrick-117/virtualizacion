import tkinter as tk 

class Semaforo:
    def __init__(self, root):  # Corrige __init__
        self.root = root
        self.root.title("Semáforo Variante 2") 

        # Crear el contenedor del semáforo
        self.canvas = tk.Canvas(root, width=1000, height=1200, bg='lightgrey')
        self.canvas.pack() 

        # Crear el paisaje
        self.canvas.create_rectangle(0, 700, 1000, 1200, fill='forestgreen')  # Césped
        self.canvas.create_rectangle(0, 600, 1000, 700, fill='lightblue')  # Cielo 

        # Crear la carretera para carros naranjas
        self.canvas.create_rectangle(0, 850, 1000, 950, fill='black')  # Carretera naranja
        self.canvas.create_line(500, 850, 500, 950, fill='white', width=4)  # Línea blanca vertical en el centro 

        # Crear la carretera para carros grises
        self.canvas.create_rectangle(0, 750, 1000, 850, fill='black')  # Carretera gris
        self.canvas.create_line(500, 750, 500, 850, fill='white', width=4)  # Línea blanca vertical en el centro 

        # Crear una línea blanca horizontal para separar las filas de carros
        self.canvas.create_line(0, 900, 1000, 900, fill='white', width=4)  # Línea blanca horizontal en el medio de la carretera naranja 

        # Crear las luces del semáforo
        self.red_light = self.canvas.create_oval(20, 20, 80, 100, fill='grey')
        self.yellow_light = self.canvas.create_oval(20, 120, 80, 200, fill='grey')
        self.green_light = self.canvas.create_oval(20, 220, 80, 300, fill='grey') 

        # Mover el semáforo a una nueva ubicación
        self.canvas.create_rectangle(300, 20, 320, 300, fill='black')  # Base del semáforo
        self.canvas.move(self.red_light, 280, 0)
        self.canvas.move(self.yellow_light, 280, 0)
        self.canvas.move(self.green_light, 280, 0) 

        # Crear las vías separadas para los carros
        self.canvas.create_rectangle(0, 850, 500, 950, fill='darkgrey')  # Vía para carros naranjas
        self.canvas.create_rectangle(500, 750, 1000, 850, fill='darkgrey')  # Vía para carros grises 

        # Crear los carros en filas horizontales
        self.cars_orange = [
            self.canvas.create_rectangle(10, 860, 60, 890, fill='orange', outline='black'),  # Carro naranja 1
            self.canvas.create_rectangle(90, 860, 140, 890, fill='orange', outline='black'),  # Carro naranja 2
            self.canvas.create_rectangle(170, 860, 220, 890, fill='orange', outline='black'),  # Carro naranja 3
            self.canvas.create_rectangle(250, 860, 300, 890, fill='orange', outline='black'),  # Carro naranja 4
            self.canvas.create_rectangle(330, 860, 380, 890, fill='orange', outline='black'),  # Carro naranja 5
            self.canvas.create_rectangle(410, 860, 460, 890, fill='orange', outline='black'),  # Carro naranja 6
            self.canvas.create_rectangle(490, 860, 540, 890, fill='orange', outline='black'),  # Carro naranja 7
            self.canvas.create_rectangle(570, 860, 620, 890, fill='orange', outline='black'),  # Carro naranja 8
            self.canvas.create_rectangle(650, 860, 700, 890, fill='orange', outline='black'),  # Carro naranja 9
            self.canvas.create_rectangle(730, 860, 780, 890, fill='orange', outline='black')   # Carro naranja 10
        ] 

        self.cars_grey = [
            self.canvas.create_rectangle(510, 760, 560, 790, fill='grey', outline='black'),  # Carro gris 1
            self.canvas.create_rectangle(590, 760, 640, 790, fill='grey', outline='black'),  # Carro gris 2
            self.canvas.create_rectangle(670, 760, 720, 790, fill='grey', outline='black'),  # Carro gris 3
            self.canvas.create_rectangle(750, 760, 800, 790, fill='grey', outline='black'),  # Carro gris 4
            self.canvas.create_rectangle(830, 760, 880, 790, fill='grey', outline='black'),  # Carro gris 5
            self.canvas.create_rectangle(910, 760, 960, 790, fill='grey', outline='black'),  # Carro gris 6
            self.canvas.create_rectangle(10, 770, 60, 800, fill='grey', outline='black'),  # Carro gris 7
            self.canvas.create_rectangle(90, 770, 140, 800, fill='grey', outline='black'),  # Carro gris 8
            self.canvas.create_rectangle(170, 770, 220, 800, fill='grey', outline='black'),  # Carro gris 9
            self.canvas.create_rectangle(250, 770, 300, 800, fill='grey', outline='black')   # Carro gris 10
        ] 

        # Iniciar el ciclo del semáforo
        self.estado = "ROJO"
        self.actualizar() 

    def actualizar(self):
        self.cambiar_color()
        self.mostrar_estado()
        self.root.after(15000, self.actualizar)  # Cambiar cada 15 segundos 

    def mostrar_estado(self):
        self.reset_lights()
        if self.estado == "ROJO":
            self.canvas.itemconfig(self.red_light, fill='red')
            self.detener_carros()
        elif self.estado == "AMARILLO":
            self.canvas.itemconfig(self.yellow_light, fill='yellow')
            self.mover_carros(lento=True)
        elif self.estado == "VERDE":
            self.canvas.itemconfig(self.green_light, fill='green')
            self.mover_carros(lento=False) 

    def cambiar_color(self):
        if self.estado == "ROJO":
            self.estado = "VERDE"
        elif self.estado == "VERDE":
            self.estado = "AMARILLO"
        elif self.estado == "AMARILLO":
            self.estado = "ROJO" 

    def reset_lights(self):
        self.canvas.itemconfig(self.red_light, fill='grey')
        self.canvas.itemconfig(self.yellow_light, fill='grey')
        self.canvas.itemconfig(self.green_light, fill='grey') 

    def mover_carros(self, lento):
        # Mover los carros según el estado de la luz
        velocidad = 5 if not lento else 2  # Velocidad normal o lenta 

        # Mover los carros naranjas hacia la izquierda
        for car in self.cars_orange:
            x1, y1, x2, y2 = self.canvas.coords(car)
            if x2 < 0:
                self.canvas.coords(car, 1000, y1, 1050, y2)  # Reiniciar posición
            else:
                self.canvas.move(car, -velocidad, 0) 

        # Mover los carros grises hacia la derecha
        for car in self.cars_grey:
            x1, y1, x2, y2 = self.canvas.coords(car)
            if x1 > 1000:
                self.canvas.coords(car, -50, y1, 0, y2)  # Reiniciar posición
            else:
                self.canvas.move(car, velocidad, 0) 

        if self.estado != "ROJO":
            self.root.after(100, self.mover_carros, lento)  # Seguir moviendo los carros 

    def detener_carros(self):
        # Detener los carros si están en la zona de la carretera cuando la luz está en rojo
        for car in self.cars_orange:
            x1, y1, x2, y2 = self.canvas.coords(car)
            if 0 <= x2 <= 500:
                self.canvas.coords(car, x1, y1, x2, y2)  # Mantener el carro en la misma posición 

        for car in self.cars_grey:
            x1, y1, x2, y2 = self.canvas.coords(car)
            if 500 <= x1 <= 1000:
                self.canvas.coords(car, x1, y1, x2, y2)  # Mantener el carro en la misma posición 

# Crear la ventana principal
root = tk.Tk()
semaforo = Semaforo(root) 

# Iniciar el bucle principal de la ventana
root.mainloop()