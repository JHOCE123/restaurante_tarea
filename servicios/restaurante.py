from modelos.producto import Producto
from modelos.cliente import Cliente

class Restaurante:
    def __init__(self, nombre_establecimiento: str):
        self.nombre_establecimiento= nombre_establecimiento
        self.lista_productos: list[Producto] = []
        self.lista_clientes: list[Cliente] = []

    def registrar_producto(self, producto: Producto) -> None:
        self.lista_productos.append(producto)

    def registrar_cliente(self, cliente: Cliente) -> None:
        self.lista_clientes.append(cliente)

    def mostrar_reporte_general(self) -> None:
        print(f"\n--- REPORTE GENERAL: {self.nombre_establecimiento.upper()} ---")
        print("\n[Menú de Productos]")
        for prod in self.lista_productos:
            print(f" - {prod}")
        print("\n[Clientes Activos]")
        for cli in self.lista_clientes:
            print(f" - {cli}")