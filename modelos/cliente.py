class Cliente:
    def __init__(self, nombre: str, mesa: int, es_frecuente: bool):
        self.nombre = nombre
        self.mesa= mesa
        self.es_frecuente= es_frecuente

    def __str__(self) -> str:
        tipo = "Frecuente" if self.es_frecuente else "Regular"
        return f"Cliente: {self.nombre} | Mesa: {self.mesa} | Tipo: {tipo}"