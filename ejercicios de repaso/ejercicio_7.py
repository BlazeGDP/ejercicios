if __name__ == "__main__":
    lista = []
    cantidad = int(input("¿cuantos numeros deseas ingresar?: "))
    i = 1
    while i <= cantidad:
        n = int(input(f"{i} ingrese un numero: "))
        lista.append(n)
        i += 1
    print("numero mayor ", max(lista))
    print("numero menor ", min(lista))



