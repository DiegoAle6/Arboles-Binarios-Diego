class NodoArbol:
    def __init__(self, dato):
        self.dato = dato
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, dato):
        if self.raiz is None:
            self.raiz = NodoArbol(dato)
        else:
            self._insertar_recursivo(self.raiz, dato)

    def _insertar_recursivo(self, nodo, nuevo_dato):
        if nuevo_dato < nodo.dato:
            if nodo.izquierda is None:
                nodo.izquierda = NodoArbol(nuevo_dato)
            else:
                self._insertar_recursivo(nodo.izquierda, nuevo_dato)
        else:
            if nodo.derecha is None:
                nodo.derecha = NodoArbol(nuevo_dato)
            else:
                self._insertar_recursivo(nodo.derecha, nuevo_dato)

    def mostrar_arbol(self):
        self._mostrar_arbol_recursivo(self.raiz, 0)

    def _mostrar_arbol_recursivo(self, nodo, nivel):
        if nodo is not None:
            self._mostrar_arbol_recursivo(nodo.derecha, nivel + 1)
            print("      " * nivel + str(nodo.dato))
            self._mostrar_arbol_recursivo(nodo.izquierda, nivel + 1)

    def buscar(self, dato):
        return self._buscar_recursivo(self.raiz, dato)

    def _buscar_recursivo(self, nodo, dato):
        if nodo is None or nodo.dato == dato:
            return nodo
        if dato < nodo.dato:
            return self._buscar_recursivo(nodo.izquierda, dato)
        return self._buscar_recursivo(nodo.derecha, dato)

    def eliminar(self, dato):
        self.raiz = self._eliminar_recursivo(self.raiz, dato)

    def _eliminar_recursivo(self, nodo, dato):
        if nodo is None:
            return nodo
        if dato < nodo.dato:
            nodo.izquierda = self._eliminar_recursivo(nodo.izquierda, dato)
        elif dato > nodo.dato:
            nodo.derecha = self._eliminar_recursivo(nodo.derecha, dato)
        else:
            if nodo.izquierda is None:
                return nodo.derecha
            elif nodo.derecha is None:
                return nodo.izquierda
            nodo.dato = self._encontrar_minimo(nodo.derecha)
            nodo.derecha = self._eliminar_recursivo(nodo.derecha, nodo.dato)
        return nodo

    def _encontrar_minimo(self, nodo):
        actual = nodo
        while actual.izquierda is not None:
            actual = actual.izquierda
        return actual.dato

    def recorrer_preOrden(self):
        resultado = []
        self._preOrden_recursivo(self.raiz, resultado)
        return resultado

    def _preOrden_recursivo(self, nodo, resultado):
        if nodo is not None:
            resultado.append(nodo.dato)
            self._preOrden_recursivo(nodo.izquierda, resultado)
            self._preOrden_recursivo(nodo.derecha, resultado)

    def recorrer_inOrden(self):
        resultado = []
        self._inOrden_recursivo(self.raiz, resultado)
        return resultado

    def _inOrden_recursivo(self, nodo, resultado):
        if nodo is not None:
            self._inOrden_recursivo(nodo.izquierda, resultado)
            resultado.append(nodo.dato)
            self._inOrden_recursivo(nodo.derecha, resultado)

    def recorrer_postOrden(self):
        resultado = []
        self._postOrden_recursivo(self.raiz, resultado)
        return resultado

    def _postOrden_recursivo(self, nodo, resultado):
        if nodo is not None:
            self._postOrden_recursivo(nodo.izquierda, resultado)
            self._postOrden_recursivo(nodo.derecha, resultado)
            resultado.append(nodo.dato)

def mostrar_menu():
    print("1. Insertar elemento")
    print("2. Mostrar árbol")
    print("3. Buscar elemento")
    print("4. Eliminar elemento")
    print("5. Recorrer en preorden")
    print("6. Recorrer en inorden")
    print("7. Recorrer en postorden")
    print("8. Salir")

def main():
    arbol = ArbolBinario()

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            elemento = int(input("Ingrese el elemento a insertar: "))
            arbol.insertar(elemento)
        elif opcion == "2":
            arbol.mostrar_arbol()
        elif opcion == "3":
            elemento = int(input("Ingrese el elemento a buscar: "))
            if arbol.buscar(elemento):
                print(f"El elemento {elemento} está en el árbol.")
            else:
                print(f"El elemento {elemento} no está en el árbol.")
        elif opcion == "4":
            elemento = int(input("Ingrese el elemento a eliminar: "))
            arbol.eliminar(elemento)
        elif opcion == "5":
            print("Preorden:", arbol.recorrer_preOrden())
        elif opcion == "6":
            print("Inorden:", arbol.recorrer_inOrden())
        elif opcion == "7":
            print("Postorden:", arbol.recorrer_postOrden())
        elif opcion == "8":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
