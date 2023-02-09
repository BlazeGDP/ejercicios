if __name__ == "__main__":
  def operaciones():
    a = int(input("Ingrese primer numero: \n"))
    b = int(input("Ingrese segundo numero: \n"))
    return f"La suma es {a+b}, la multiplicacion es {a*b}, la resta es {a-b} y la division es {a/b}"
print(f"Las operaciones numeros ingresados son: ", operaciones())
