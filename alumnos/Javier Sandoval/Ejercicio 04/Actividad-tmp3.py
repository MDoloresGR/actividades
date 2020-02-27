T = [[11, 12, 5, 2], [15, 6, 10], [10, 8, 12, 5], [12, 15, 8, 6]]
for r in T: #se refiere a una de las listas, o renglones
  for c in r: #se refiere a la columna, o la posicion del elemento dentro del renglón
    print(c,end = " ") #Esta linea es para establecer el acomodo en que van a aperecer los números: cuando termina, agrega un espacio en blanco
  print()