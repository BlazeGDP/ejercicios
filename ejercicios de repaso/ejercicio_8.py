if __name__ == "__main__":
    lista = []
    cantidad = int(input("¿cuantos numeros deseas ingresar?: "))
    i = 1
    while i <= cantidad:
        n = int(input(f"{i} ingrese un numero: "))
        lista.append(n)
        i += 1
    lista2 = lista[::-1]
    print(f"La lista original es: {lista} y su inversion seria: {lista2}")

