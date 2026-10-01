import re


class Simbolo:
    def __init__(self, nombre, tipo, uso, direccion):
        self.nombre = nombre
        self.tipo = tipo
        self.uso = uso
        self.direccion = direccion


class TablaSimbolos:
    def __init__(self):
        self.simbolos = {}
        self.siguiente_direccion = 1000

    def declarar(self, nombre, tipo):

        if nombre in self.simbolos:
            raise SemanticError(
                f"El identificador '{nombre}' ya fue declarado."
            )

        self.simbolos[nombre] = Simbolo(
            nombre,
            tipo,
            "variable",
            self.siguiente_direccion
        )

        self.siguiente_direccion += 4

    def obtener(self, nombre):

        if nombre not in self.simbolos:
            raise SemanticError(
                f"El identificador '{nombre}' no ha sido declarado."
            )

        return self.simbolos[nombre]

    def mostrar(self):

        print("\nTABLA DE SÍMBOLOS")
        print("-" * 60)
        print(
            f"{'Nombre':<15}"
            f"{'Tipo':<12}"
            f"{'Uso':<15}"
            f"{'Dirección'}"
        )

        for simbolo in self.simbolos.values():

            print(
                f"{simbolo.nombre:<15}"
                f"{simbolo.tipo:<12}"
                f"{simbolo.uso:<15}"
                f"{simbolo.direccion}"
            )


class SemanticError(Exception):
    pass


def procesar(programa):

    tabla = TablaSimbolos()

    errores = []

    lineas = programa.strip().splitlines()

    for numero, linea in enumerate(lineas, 1):

        linea = linea.strip()

        try:

            # Declaraciones

            declaracion = re.fullmatch(
                r"(int|float)\s+([A-Za-z_]\w*)\s*;",
                linea
            )

            if declaracion:

                tipo = declaracion.group(1)
                nombre = declaracion.group(2)

                tabla.declarar(nombre, tipo)

                continue

            # Asignaciones

            asignacion = re.fullmatch(
                r"([A-Za-z_]\w*)\s*=\s*(.+);",
                linea
            )

            if asignacion:

                destino = asignacion.group(1)
                expresion = asignacion.group(2)

                tabla.obtener(destino)

                identificadores = re.findall(
                    r"[A-Za-z_]\w*",
                    expresion
                )

                for identificador in identificadores:
                    tabla.obtener(identificador)

                continue

            raise SemanticError(
                "Sentencia no reconocida."
            )

        except SemanticError as error:

            errores.append(
                f"Línea {numero}: {error}"
            )

    return tabla, errores


def main():

    programa = """
int x;
float y;
x = 10;
y = x + 2.5;
z = x + 1;
"""

    tabla, errores = procesar(programa)

    tabla.mostrar()

    print("\nERRORES SEMÁNTICOS")

    if errores:

        for error in errores:
            print("-", error)

    else:
        print("No se detectaron errores.")


if __name__ == "__main__":
    main()