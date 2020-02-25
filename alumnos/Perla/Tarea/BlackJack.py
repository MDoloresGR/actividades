jug1 = [1, 8, 11, 10, 7]
jug2 = [2, 6, 8, 12, 4]
jug3 = [3, 7, 1, 5, 10]
jug4 = [4, 10, 11, 3, 10]
jug1.reverse()
jug2.reverse()
jug3.reverse()
jug4.reverse()
numcarta = 0
empate = 0
ganador = 0
puntosjug1 = 0
puntosjug2 = 0
puntosjug3 = 0
puntosjug4 = 0
for carta in jug1:
  if jug1[numcarta] >= jug2[numcarta]:
      if jug1[numcarta] >= jug3[numcarta]:
          if jug1[numcarta] >= jug4[numcarta]:
            puntosjug1 = puntosjug1 + 1
            if jug1[numcarta] == jug2[numcarta]:
              puntosjug2 = puntosjug2 + 1
            if jug1[numcarta] == jug3[numcarta]:
              puntosjug3 = puntosjug3 + 1
            if jug1[numcarta] == jug4[numcarta]:
              puntosjug4 = puntosjug4 + 1
          else:
            puntosjug4 = puntosjug4 + 1
      else:
        if jug3[numcarta] >= jug4[numcarta]:
          puntosjug3 = puntosjug3 + 1
          if jug3[numcarta] == jug4[numcarta]:
            puntosjug4 = puntosjug4 + 1
        else:
          puntosjug4 = puntosjug4 + 1
  else:
    if jug2[numcarta] >= jug3[numcarta]:
        if jug2[numcarta] >= jug4[numcarta]:
          puntosjug2 = puntosjug2 + 1
          if jug2[numcarta] == jug4[numcarta]:
            puntosjug4 = puntosjug4 + 1
    else: 
      if jug3[numcarta] >= jug4[numcarta]:
        puntosjug3 = puntosjug3 + 1
        if jug3[numcarta] == jug4[numcarta]:
          puntosjug4 = puntosjug4 + 1
      else:
        puntosjug4 = puntosjug4 + 1
  numcarta = numcarta + 1   
if puntosjug1 >= puntosjug2:
  if puntosjug1 >= puntosjug3:
    if puntosjug1 >= puntosjug4:
      if (puntosjug1 == puntosjug2) or (puntosjug1 ==   puntosjug3) or (puntosjug1 == puntosjug4):
        empate = 1
      else:
        ganador = 1
    else:
      ganador = 4  
  else:
    if puntosjug3 >= puntosjug4:
      if (puntosjug3 == puntosjug4):
        empate = 1
      else:
        gandor = 3  
    else:
      ganador = 4 
else:
  if puntosjug2 >= puntosjug3:
    if puntosjug2 >= puntosjug4:
      if (puntosjug2 == puntosjug3) or (puntosjug2 ==   puntosjug4):
        empate = 1
      else:
        ganador = 2
    else:
      if puntosjug2 == puntosjug4:
        empate = 1
      else:
        ganador = 4
  else:
    if puntosjug3 >= puntosjug4:
      if puntosjug3 == puntosjug4:
        empate = 1
      else:
        ganador = 3
    else:
      ganador = 4
if empate > 0:
  print("Empate, no hay ganador")
else:
  print("el ganador es el jugador: " + str(ganador))