def matriz(arreglo_inicial):
    """Inserta los 6 elementos base en una lista de listas de 2x3."""
    matriz_destino = [["" for _ in range(3)] for _ in range(2)]
    indice = 0
    for i in range(2):
        for j in range(3):
            matriz_destino[i][j] = arreglo_inicial[indice]
            indice += 1
    return matriz_destino

def pila(arreglo_inicial):
    """Usa una lista de Python simulando la estructura LIFO y le añade 2 nuevos elementos."""
    mi_pila = []
    # Almacenar los 6 valores iniciales
    for pelicula in arreglo_inicial:
        mi_pila.append(pelicula)
    
    # Agregar 2 películas adicionales
    mi_pila.append("El Padrino")
    mi_pila.append("Pulp Fiction")
    return mi_pila

def imprimir_finales(mat, stack):
    """Función aislada de visualización de datos finales en terminal."""
    print("\n--- Valores de la Matriz (2x3) ---")
    for i in range(2):
        fila = ""
        for j in range(3):
            fila += f"[{mat[i][j]}] "
        print(fila)
    
    print("\n--- Valores de la Pila ---")
    # Copiar para poder vaciar la pila usando pop() sin afectar el programa principal
    temp_stack = stack.copy()
    while temp_stack:
        print(temp_stack.pop())
    print("----------------------------------")

def main():
    # 6 variables predefinidas bajo el contexto de películas
    peliculas = ["Interstellar", "El Origen", "Matrix", "Gladiador", "Titanic", "Avatar"]
    mat_resultante = None
    pila_resultante = None

    while True:
        print("\n=== Menú Principal - MisGustosAlejandro ===")
        print("1. Generar Matriz de Películas")
        print("2. Generar Pila de Películas")
        print("3. Imprimir Valores Finales")
        print("4. Salir")
        
        # Validación de tipo Try-Except para entradas numéricas
        try:
            opcion = int(input("Ingrese su elección: "))
        except ValueError:
            print("Error: Entrada no válida. Por favor, ingrese un número entero.")
            continue

        # Estructuras lógicas de control 
        if opcion == 1:
            mat_resultante = matriz(peliculas)
            print("Matriz 2x3 estructurada correctamente.")
        elif opcion == 2:
            pila_resultante = pila(peliculas)
            print("Pila generada y poblada con 8 elementos totales.")
        elif opcion == 3:
            if mat_resultante is not None and pila_resultante is not None:
                imprimir_finales(mat_resultante, pila_resultante)
            else:
                print("Atención: Es obligatorio llenar la matriz y la pila (opciones 1 y 2) antes de imprimir.")
        elif opcion == 4:
            print("Finalizando ejecución. ¡Hasta pronto!")
            break
        else:
            print("Opción incorrecta. Seleccione un número de nuestro menú (1-4).")

if __name__ == "__main__":
    main()
