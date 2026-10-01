import re


class SemanticError(Exception):
    pass


class TablaSimbolos:
    def __init__(self):
        self.simbolos = {}

    def declarar(self, nombre, tipo):

        if nombre in self.simbolos:
            raise SemanticError(
                f"'{nombre}' ya fue declarado."
            )

        self.simbolos[nombre] = tipo

    def tipo(self, nombre):

        if nombre not in self.simbolos:
            raise SemanticError(
                f"'{nombre}' no está declarado."
            )

        return self.simbolos[nombre]


def tipo_operando(operando, tabla):

    if re.fullmatch(r"\d+", operando):
        return "int"

    if re.fullmatch(r"\d+\.\d+", operando):
        return "float"

    return tabla.tipo(operando)


def tipo_expresion(expresion, tabla):

    operandos = re.findall(
        r"[A-Za-z_]\w*|\d+\.\d+|\d+",
        expresion
    )

    tipos = [
        tipo_operando(op, tabla)
        for op in operandos
    ]

    if "float" in tipos:
        return "float"

    return "int"


def main():

    tabla = TablaSimbolos()

    tabla.declarar("a", "int")
    tabla.declarar("b", "float")

    pruebas = [
        ("a", "10 + 5"),
        ("b", "a + 2.5"),
        ("a", "b + 1.2")
    ]

    for destino, expresion in pruebas:

        print(
            f"\n{destino} = {expresion};"
        )

        try:

            tipo_destino = tabla.tipo(destino)
            tipo_expr = tipo_expresion(
                expresion,
                tabla
            )

            print(
                "Tipo destino:",
                tipo_destino
            )

            print(
                "Tipo expresión:",
                tipo_expr
            )

            if (
                tipo_destino == "int"
                and tipo_expr == "float"
            ):

                raise SemanticError(
                    "No se puede asignar float a int."
                )

            print("Sentencia semánticamente válida.")

        except SemanticError as error:

            print(
                "ERROR SEMÁNTICO:",
                error
            )


if __name__ == "__main__":
    main()