class Generador:

    def __init__(self):

        self.temporal = 0
        self.codigo = []

    def nuevo_temp(self):

        self.temporal += 1

        return f"t{self.temporal}"

    def suma(self, a, b):

        t = self.nuevo_temp()

        self.codigo.append(
            f"{t} = {a} + {b}"
        )

        return t

    def multiplicacion(self, a, b):

        t = self.nuevo_temp()

        self.codigo.append(
            f"{t} = {a} * {b}"
        )

        return t


def probar_1():

    g = Generador()

    # a + b

    resultado = g.suma(
        "a",
        "b"
    )

    return g.codigo, resultado


def probar_2():

    g = Generador()

    # a + b * c

    t1 = g.multiplicacion(
        "b",
        "c"
    )

    t2 = g.suma(
        "a",
        t1
    )

    return g.codigo, t2


def probar_3():

    g = Generador()

    # a * b + c

    t1 = g.multiplicacion(
        "a",
        "b"
    )

    t2 = g.suma(
        t1,
        "c"
    )

    return g.codigo, t2


def main():

    pruebas = [
        ("a + b", probar_1),
        ("a + b * c", probar_2),
        ("a * b + c", probar_3)
    ]

    for nombre, funcion in pruebas:

        print(
            "\nExpresión:",
            nombre
        )

        codigo, resultado = funcion()

        for linea in codigo:
            print(linea)

        print(
            "Resultado en:",
            resultado
        )


if __name__ == "__main__":
    main()