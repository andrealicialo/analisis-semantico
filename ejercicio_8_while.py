class Generador:

    def __init__(self):

        self.etiqueta = 0
        self.temporal = 0
        self.codigo = []

    def nueva_etiqueta(self):

        self.etiqueta += 1

        return f"L{self.etiqueta}"

    def nuevo_temporal(self):

        self.temporal += 1

        return f"t{self.temporal}"


def main():

    g = Generador()

    inicio = g.nueva_etiqueta()
    fin = g.nueva_etiqueta()

    t1 = g.nuevo_temporal()
    t2 = g.nuevo_temporal()

    g.codigo.append(
        f"{inicio}:"
    )

    g.codigo.append(
        f"ifFalse i < 10 goto {fin}"
    )

    g.codigo.append(
        f"{t1} = suma + i"
    )

    g.codigo.append(
        f"suma = {t1}"
    )

    g.codigo.append(
        f"{t2} = i + 1"
    )

    g.codigo.append(
        f"i = {t2}"
    )

    g.codigo.append(
        f"goto {inicio}"
    )

    g.codigo.append(
        f"{fin}:"
    )

    print("=" * 65)
    print("EJERCICIO 8 - WHILE")
    print("=" * 65)

    for linea in g.codigo:
        print(linea)


if __name__ == "__main__":
    main()