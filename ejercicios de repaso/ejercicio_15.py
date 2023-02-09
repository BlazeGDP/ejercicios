if __name__ == "__main__":
    mensaje = input("ingresar su mensaje: ")

    def pali(mensaje):
        aux = ""
        for i in range(len(mensaje)-1, -1, -1):
            aux += mensaje[i]

        if mensaje == aux:
            x = print(f"{mensaje} y {aux} son palindromos")
        else:
            x = print(f"{mensaje} y {aux} no son palindromos")
        return x
    pali(mensaje)