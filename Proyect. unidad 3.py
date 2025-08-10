# unidad3_bucles.py
"""
Proyecto: Unidad 3 - Bucles
Autor: Gabriel Campaña 
Descripción:
 Módulo con ejemplos y utilidades que implementan los contenidos de la Unidad 3:
 - for, while
 - bucles anidados
 - break / continue
 - estructuras lógicas y validaciones
 - comentarios y docstrings
"""

from typing import List
import random

# -----------------------
# Funciones con bucles
# -----------------------

def suma_numeros_for(n: int) -> int:
    """
    Suma n números ingresados por el usuario usando un bucle for.
    Demuestra uso de for con range() cuando conocemos el número de iteraciones.
    """
    total = 0
    for i in range(n):
        while True:
            try:
                m = int(input(f"Ingrese el número {i+1}: "))
                break
            except ValueError:
                print("Entrada inválida. Intenta de nuevo (debe ser entero).")
        total += m
    return total


def suma_numeros_while() -> int:
    """
    Suma n números usando while. Demuestra control con condición variable.
    """
    total = 0
    while True:
        try:
            n = int(input("¿Cuántos números deseas sumar?: "))
            if n <= 0:
                print("Ingresa un número mayor que 0.")
                continue
            break
        except ValueError:
            print("Entrada inválida.")
    i = 0
    while i < n:
        while True:
            try:
                m = int(input(f"Ingrese el número {i+1}: "))
                break
            except ValueError:
                print("Entrada inválida.")
        total += m
        i += 1
    return total


def contar_caracter(palabra: str, caracter: str) -> int:
    """
    Cuenta cuántas veces aparece 'caracter' en 'palabra' usando for.
    Ejemplo simple de iteración sobre cadenas.
    """
    contador = 0
    for letra in palabra:
        if letra == caracter:
            contador += 1
    return contador


def tablas_multiplicar(hasta: int = 10, max_factor: int = 12) -> None:
    """
    Muestra tablas de multiplicar desde 1 hasta 'hasta' (no inclusive si range se usa así),
    y factores desde 1 hasta 'max_factor'. Demuestra bucle anidado for-for.
    """
    print(f"Tablas del 1 al {hasta}:")
    for x in range(1, hasta + 1):
        print(f"Tabla del {x}:")
        for y in range(1, max_factor + 1):
            print(f"{x} x {y} = {x*y}")
        print("-" * 12)


def buscar_y_break(palabra: str, objetivo: str) -> int:
    """
    Busca el primer índice de 'objetivo' en 'palabra' usando for y break.
    Retorna el índice (0-based) o -1 si no se encuentra.
    El uso de break termina el bucle en el primer hallazgo.
    """
    for idx, ch in enumerate(palabra):
        if ch == objetivo:
            return idx
    return -1


def demonstrate_continue(palabra: str) -> List[str]:
    """
    Devuelve una lista de letras de 'palabra' excepto las vocales
    (demostración práctica del uso de 'continue').
    """
    resultado = []
    vocales = "aeiouAEIOU"
    for letra in palabra:
        if letra in vocales:
            # saltar vocales
            continue
        resultado.append(letra)
    return resultado


def juego_adivina_numero(intentos_max: int = 5):
    """
    Juego simple que usa while y control de intentos.
    Demuestra uso de bucle condicional, estructuras lógicas y break.
    """
    numero = random.randint(1, 50)
    print("He elegido un número entre 1 y 50. Tienes", intentos_max, "intentos.")
    intentos = 0
    while intentos < intentos_max:
        intentos += 1
        try:
            adivina = int(input(f"Intento {intentos}: Ingresa tu número: "))
        except ValueError:
            print("Entrada inválida, intenta con un número entero.")
            continue
        if adivina == numero:
            print(f"¡Felicidades! Adivinaste en {intentos} intentos.")
            break
        elif adivina < numero:
            print("Más alto.")
        else:
            print("Más bajo.")
    else:
        # Se ejecuta si el while terminó sin break (esto es un uso de else en bucles)
        print(f"Se acabaron los intentos. El número era {numero}.")


def generar_matriz_transpuesta(filas: int, columnas: int) -> List[List[int]]:
    """
    Genera una matriz (lista de listas) con valores secuenciales y
    devuelve su transpuesta. Demuestra bucles anidados y manipulación de listas.
    """
    matriz = []
    val = 1
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(val)
            val += 1
        matriz.append(fila)

    # calcular transpuesta
    transpuesta = []
    for c in range(columnas):
        nueva_fila = []
        for r in range(filas):
            nueva_fila.append(matriz[r][c])
        transpuesta.append(nueva_fila)

    return transpuesta


def es_primo(n: int) -> bool:
    """
    Verificación simple de número primo usando bucle for y lógica.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def lista_primos_hasta(n: int) -> List[int]:
    """
    Genera todos los números primos hasta n (incluido) usando for y la función es_primo.
    Demuestra mezcla de funciones y bucles.
    """
    primos = []
    for i in range(2, n + 1):
        if es_primo(i):
            primos.append(i)
    return primos


# -----------------------
# Interfaz simple de consola (menú)
# -----------------------
def menu():
    """
    Menú que permite probar las distintas funciones. Implementado con while True y break.
    """
    while True:
        print("\n--- MENU: Unidad 3 - Bucles ---")
        print("1) Suma con for (n números)")
        print("2) Suma con while (n números)")
        print("3) Contar carácter")
        print("4) Tablas de multiplicar")
        print("5) Buscar letra (break)")
        print("6) Demostrar continue (eliminar vocales)")
        print("7) Juego: Adivina el número")
        print("8) Generar transpuesta de matriz")
        print("9) Lista de primos hasta n")
        print("0) Salir")
        opcion = input("Elige una opción: ").strip()
        if opcion == "1":
            n = int(input("¿Cuántos números?: "))
            print("Resultado:", suma_numeros_for(n))
        elif opcion == "2":
            print("Resultado:", suma_numeros_while())
        elif opcion == "3":
            palabra = input("Ingrese palabra: ")
            caracter = input("¿Qué carácter contar?: ")
            print("Veces:", contar_caracter(palabra, caracter))
        elif opcion == "4":
            hasta = int(input("Tablas hasta (ej. 10): "))
            tablas_multiplicar(hasta)
        elif opcion == "5":
            palabra = input("Ingresa palabra: ")
            objetivo = input("Carácter a buscar: ")
            idx = buscar_y_break(palabra, objetivo)
            if idx >= 0:
                print(f"Encontrado en índice {idx}")
            else:
                print("No encontrado")
        elif opcion == "6":
            palabra = input("Ingresa palabra: ")
            print("Sin vocales:", "".join(demonstrate_continue(palabra)))
        elif opcion == "7":
            juego_adivina_numero()
        elif opcion == "8":
            f = int(input("Filas: "))
            c = int(input("Columnas: "))
            trans = generar_matriz_transpuesta(f, c)
            print("Transpuesta:")
            for row in trans:
                print(row)
        elif opcion == "9":
            n = int(input("Hasta qué número?: "))
            print("Primos:", lista_primos_hasta(n))
        elif opcion == "0":
            print("Saliendo. ¡Éxitos con tu proyecto!")
            break
        else:
            print("Opción inválida. Intenta otra vez.")


if __name__ == "__main__":
    menu()


