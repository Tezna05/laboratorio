class CarritoDeCompras:
    def __init__(self):
        self.productos = []  

    def agregar_producto(self, producto):
        self.productos.append(producto)
        print(f"Has agregado {producto} al carrito.")

    def eliminar_producto(self, producto):
        if producto in self.productos:
            self.productos.remove(producto)
            print(f"Has eliminado {producto} del carrito.")
        else:
            print(f"{producto} no está en el carrito.")

    def mostrar_carrito(self):
        if self.productos:
            print("Productos en el carrito:")
            for producto in self.productos:
                print(f"- {producto}")
        else:
            print("El carrito está vacío.")
carrito = CarritoDeCompras()
carrito.mostrar_carrito()          
carrito.agregar_producto("pera")   
carrito.agregar_producto("tomate")       
carrito.mostrar_carrito()         
carrito.eliminar_producto("tomate")       
carrito.mostrar_carrito()         
carrito.eliminar_producto("alchol")    
