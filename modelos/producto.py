class Producto:
    def __init__(self, nombre: str, precio: float, disponible: bool):
        self.nombre= nombre
        self.precio = precio
        self.disponible= disponible

    def __str__(self) -> str:
        estado = "Disponible" if self.disponible else "Agotado"
        return f"Producto: {self.nombre} | Precio: ${self.precio:.2f} | Estado: {estado}"