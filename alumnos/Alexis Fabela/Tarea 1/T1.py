print("Tarea 1")

print("Manos mostradas para cada jugador"'\n')
P1 = [8, 4, 3, 5, 7]
P2 = [4, 5, 2, 1, 6]
P3 = [2, 8 ,4, 9, 1]
P4 = [3, 11, 1, 10, 13]

print("Se muestra la ultima carta que se entrego al jugador, al terminar la ronda se van descartando")

print("Jugador 1: ", P1) 
print("Jugador 2: ", P2)
print("Jugador 3: ", P3)
print("Jugador 4: ", P4, '\n')
print("Inicio del juego" '\n')
# usar solamente el ultimo numero de la lista e ir eliminadno de acuerdo al ganador.
R1 = []
R1.append(P1[4])
R1.append(P2[4])
R1.append(P3[4])
R1.append(P4[4])
val = R1[0]

for i in range(0, len(R1)):
  if R1[i]>val:
    val = R1[i]

print("Ronda 1: ", R1, '\n')

print("Ganador: ", val, '\n')

print("Termina Ronda 1" '\n')

#Inicia ronda 2
R2 = []
R2.append(P1[3])
R2.append(P2[3])
R2.append(P3[3])
R2.append(P4[3])
val1 = R2[0]

for i in range(0, len(R2)):
  if R2[i]>val1:
    val1 = R2[i]

print("Ronda 2: ", R2, '\n')

print("Ganador: ", val1, '\n')

print("Termina Ronda 2" '\n')

#Inicia ronda 3
R3 = []
R3.append(P1[2])
R3.append(P2[2])
R3.append(P3[2])
R3.append(P4[2])
val2 = R3[0]

for i in range(0, len(R3)):
  if R3[i]>val2:
    val2 = R3[i]

print("Ronda 3: ", R3, '\n')

print("Ganador: ", val2, '\n')

print("Termina Ronda 3" '\n')

#Inicia ronda 4
R4 = []
R4.append(P1[1])
R4.append(P2[1])
R4.append(P3[1])
R4.append(P4[1])
val3 = R4[0]

for i in range(0, len(R4)):
  if R4[i]>val3:
    val3 = R4[i]

print("Ronda 4: ", R4, '\n')

print("Ganador: ", val3, '\n')

print("Termina Ronda 4" '\n')

#Inicia ronda 5
R5 = []
R5.append(P1[0])
R5.append(P2[0])
R5.append(P3[0])
R5.append(P4[0])
val4 = R5[0]

for i in range(0, len(R5)):
  if R5[i]>val4:
    val4 = R5[i]

print("Ronda 5: ", R5, '\n')

print("Ganador: ", val4, '\n')

print("Termina Ronda 5" '\n')

print("Puntos acumulados" '\n')
print("Jugador 1: 1 punto") 
print("Jugador 2: 0 puntos")
print("Jugador 3: 1 punto")
print("Jugador 4: 3 puntos"'\n')

print("Gana el jugador 4 con un total de 3 puntos")