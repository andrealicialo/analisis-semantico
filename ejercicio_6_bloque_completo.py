class Simbolo:

    def __init__(self, nombre, tipo, direccion):

        self.nombre = nombre
        self.tipo = tipo
        self.direccion = direccion


def main():

    tabla = {
        "x": Simbolo(
            "x",
            "int",
            1000
        ),

        "y": Simbolo(
            "y",
            "int",
            1004
        ),

        "promedio": Simbolo(
            "promedio",
            "float",
            1008
        )
    }

    errores = []

    codigo = [
        "x = 8",
        "y = 12",
        "t1 = x + y",
        "t2 = t1 / 2.0",
        "promedio = t2"
    ]

    print("=" * 70)
    print("EJERCICIO 6 - DECLARACIONES Y ASIGNACIONES")
    print("=" * 70)

    print("\nTABLA DE SÍMBOLOS")

    for simbolo in tabla.values():

        print(
            simbolo.nombre,
            simbolo.tipo,
            simbolo.direccion
        )

    print("\nERRORES")

    if errores:
        for error in errores:
            print(error)
    else:
        print("No existen errores semánticos.")

        print("\nCÓDIGO INTERMEDIO")

        for linea in codigo:
            print(linea)


if __name__ == "__main__":
    main()