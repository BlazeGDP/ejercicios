if __name__ == "__main__":
  def pares_cien():
    list = []
    for i in range(0, 100+1):
      if i % 2 == 0:
        list.append(i)
    return list

  def pares_cien_v2():
    list = []
    for i in range(0,100+1,2):
      list.append(i)
    return list
  print("la lista de numeros entre 1 y 100 es: ", pares_cien())
  pares_cien()
  print(pares_cien())