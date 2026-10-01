import re


class Token:

    def __init__(self, tipo, lexema, atributo=None):

        self.tipo = tipo
        self.lexema = lexema
        self.atributo = atributo

    def __str__(self):

        return (
            f"{self.tipo:<18}"
            f"{self.lexema:<12}"
            f"{self.atributo}"
        )


def tokenizar(texto):

    patron = (
        r"\d+\.\d+"
        r"|\d+"
        r"|[A-Za-z_]\w*"
        r"|[=+\-*/;]"
    )

    lexemas = re.findall(
        patron,
        texto
    )

    tokens = []

    for lexema in lexemas:

        if re.fullmatch(
            r"\d+\.\d+",
            lexema
        ):

            tokens.append(
                Token(
                    "CTE_REAL",
                    lexema,
                    float(lexema)
                )
            )

        elif lexema.isdigit():

            tokens.append(
                Token(
                    "CTE_ENTERA",
                    lexema,
                    int(lexema)
                )
            )

        elif re.fullmatch(
            r"[A-Za-z_]\w*",
            lexema
        ):

            tokens.append(
                Token(
                    "IDENTIFICADOR",
                    lexema,
                    lexema
                )
            )

        else:

            mapa = {
                "=": "ASIGNACION",
                "+": "SUMA",
                "-": "RESTA",
                "*": "MULTIPLICACION",
                "/": "DIVISION",
                ";": "FIN_SENTENCIA"
            }

            tokens.append(
                Token(
                    mapa[lexema],
                    lexema
                )
            )

    return tokens


def main():

    sentencia = "resultado = a + 2.5;"

    tokens = tokenizar(sentencia)

    print("=" * 65)
    print("EJERCICIO 3 - TOKENS Y ATRIBUTOS")
    print("=" * 65)

    print(
        f"\n{'TOKEN':<18}"
        f"{'LEXEMA':<12}"
        f"ATRIBUTO"
    )

    print("-" * 65)

    for token in tokens:
        print(token)

    print("\nComprobaciones semánticas posibles:")
    print(
        "1. El atributo del IDENTIFICADOR permite "
        "consultarlo en la tabla de símbolos."
    )
    print(
        "2. El atributo numérico permite conocer "
        "el tipo y valor de una constante."
    )


if __name__ == "__main__":
    main()