class GeneradorCodigo:

    def __init__(self):
        self.contador = 0
        self.codigo = []

    def nuevo_temporal(self):

        self.contador += 1

        return f"t{self.contador}"

    def generar_operacion(
        self,
        izquierdo,
        operador,
        derecho
    ):

        temporal = self.nuevo_temporal()

        self.codigo.append(
            f"{temporal} = "
            f"{izquierdo} {operador} {derecho}"
        )

        return temporal


def main():

    generador = GeneradorCodigo()

    # b * c primero

    t1 = generador.generar_operacion(
        "b",
        "*",
        "c"
    )

    # a + t1

    t2 = generador.generar_operacion(
        "a",
        "+",
        t1
    )

    generador.codigo.append(
        f"resultado = {t2}"
    )

    print("=" * 65)
    print("EJERCICIO 4 - CÓDIGO INTERMEDIO")
    print("=" * 65)

    print(
        "\nExpresión original:"
    )

    print(
        "resultado = a + b * c;"
    )

    print(
        "\nCódigo de tres direcciones:"
    )

    for instruccion in generador.codigo:
        print(instruccion)


if __name__ == "__main__":
    main()