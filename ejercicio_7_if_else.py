class Generador:

    def __init__(self):

        self.etiqueta = 0
        self.codigo = []

    def nueva_etiqueta(self):

        self.etiqueta += 1

        return f"L{self.etiqueta}"


def main():

    generador = Generador()

    falso = generador.nueva_etiqueta()
    fin = generador.nueva_etiqueta()

    generador.codigo.append(
        f"ifFalse a < b goto {falso}"
    )

    generador.codigo.append(
        "max = b"
    )

    generador.codigo.append(
        f"goto {fin}"
    )

    generador.codigo.append(
        f"{falso}:"
    )

    generador.codigo.append(
        "max = a"
    )

    generador.codigo.append(
        f"{fin}:"
    )

    print("=" * 65)
    print("EJERCICIO 7 - IF / ELSE")
    print("=" * 65)

    for linea in generador.codigo:
        print(linea)


if __name__ == "__main__":
    main()