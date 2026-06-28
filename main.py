from servicios.restaurante import Restaurante
from modelos.producto import Producto
from modelos.cliente import Cliente

def ejecutar_sistema():
    mi_restaurante = Restaurante("Sabores del Ecuador")

    # Creamos datos de prueba
    p1 = Producto("Encebollado Mixto", 5.50, True)
    p2 = Producto("Jugo de Maracuyá", 1.75, True)
    c1 = Cliente("Alejandro Vivar", 5, True)
    c2 = Cliente("María Elena Andrade", 12, False)

    # Los guardamos en el servicio
    mi_restaurante.registrar_producto(p1)
    mi_restaurante.registrar_producto(p2)
    mi_restaurante.registrar_cliente(c1)
    mi_restaurante.registrar_cliente(c2)

    # Imprimimos todo
    mi_restaurante.mostrar_reporte_general()

if __name__ == "__main__":
    ejecutar_sistema()