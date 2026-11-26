def infijo_a_postfijo(expresion):
    # Definición de precedencias (a mayor valor, mayor prioridad)
    precedencia = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    asociatividad_derecha = {'^'}

    pila = []  # Almacena operadores y paréntesis
    salida = []  # Resultado en notación postfijo

    # Remover espacios en blanco para procesar caracteres limpios
    tokens = expresion.replace(" ", "")

    for token in tokens:
        # Caso 1: El token es un operando (Letra o Número)
        if token.isalnum():
            salida.append(token)

        # Caso 2: Paréntesis de apertura
        elif token == '(':
            pila.append(token)

        # Caso 3: Paréntesis de cierre
        elif token == ')':
            while pila and pila[-1] != '(':
                salida.append(pila.pop())

            if pila and pila[-1] == '(':
                pila.pop()  # Eliminar el '(' residual

        # Caso 4: El token es un operador
        elif token in precedencia:
            while (pila and pila[-1] != '(' and
                   (precedencia[pila[-1]] > precedencia[token] or
                    (precedencia[pila[-1]] == precedencia[token] and token not in asociatividad_derecha))):
                salida.append(pila.pop())
            pila.append(token)

    # Vaciar los elementos restantes de la pila
    while pila:
        salida.append(pila.pop())

    return "".join(salida)

def generar_cuartetos(postfijo):
    pila = []
    cuartetos = []
    contador = 1

    operadores = ['+', '-', '*', '/', '^']

    for token in postfijo:
        if token not in operadores:
            pila.append(token)
        else:
            operando2 = pila.pop()
            operando1 = pila.pop()

            temporal = f"T{contador}"
            contador += 1

            cuartetos.append((token, operando1, operando2, temporal))
            pila.append(temporal)
    return cuartetos

# Pruebas de ejecución
if __name__ == "__main__":
    ejemplo = "A + B * C ^ D - E"

    resultado = infijo_a_postfijo(ejemplo)
    print(f"Infijo: {ejemplo} -> Postfijo: {resultado}")

    cuartetos = generar_cuartetos(resultado)
    print("\nCUARTETOS:")
    print("Operador | Operando1 | Operando2 | Resultado")
    print("---------------------------------------------")

    for c in cuartetos:
        print(f"{c[0]:^9} | {c[1]:^9} | {c[2]:^9} | {c[3]:^9}")
