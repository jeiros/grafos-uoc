def havel_hakimi(s):
  if any([x > (len(s) - 1) for x in s]):
    print("existe di > n - 1, entonces la secuencia no es grafica, fin.")
    return False
  
  while not any([x < 0 for x in s]) and s != [0]:
    # mientras no haya ningun di < 0 y s no sea identicamente 0.
    # Clasificar s en orden decreciente.
    # Eliminar d1 de s y restar 1 unidad a los d1 elementos siguientes.
    print(s)
    s.sort(reverse=True)
    print("sorted {}".format(s))
    head = s.pop(0)
    s = [x - 1 for x in s[:head]] + s[head:]
  print("finished while: {}".format(s))
  if any([x < 0 for x in s]):
    print("existe di < 0, entonces la secuencia no es grafica, fin.")
    return False
  
  if s == [0]:
    print("la secuencia resultante es la secuencia identicamente 0")
    print("s es una secuencia grafica")
    return True

if __name__ == "__main__":
    # Ejercicios
    # havel_hakimi([5,5,7,6,4,2,4,5]) # True
    # havel_hakimi([2,3,4,5,6,7,8,8,8,8,8,8,8,8,8,8]) # False
    # havel_hakimi([2,3,4,5,6,7,8,8,8,8,8,8,8,8,8,9]) # True

    # # Ejemplo
    # havel_hakimi([2,2,4,3,3,2,3,5])

    # PEC
    havel_hakimi([4, 4, 3, 2, 2, 2, 1])